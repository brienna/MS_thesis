# github.com/jbornschein/mpi4py-examples/blob/master/09-task-pull.py

# mpirun -np 5 python script3.py

# REQUIRED FILES IN ADDITION TO THIS FILE:
    # triplets.npy 
    # helper.py 
    # abstracts/*.npy

# SOME TERMINOLOGY: 

# MPI world: All of the MPI processes, spawned by `mpirun` or SLURM/srun

# MPI size: The number of MPI slots (or SLURM tasks)
    # Within a SLURM job, this is the number of tasks (--ntasks) for the job.
    # Outside of a SLURM job, this is the `-n` option given to `mpirun`. 

# MPI rank: An integer number, in the range [0, MPI size], unique to each worker. 

# This program has two parts: The controller and the worker part. 

# The controller is executed by rank 0; the workers by everyone else.

# We might have been able to use Scatterv if it accepted regular objects
# comm.scatter() is not as convenient in practice cuz it requires the size 
# of the large array to be divisible by the number of processes

from mpi4py import MPI 
import json
import numpy as np
from sklearn.model_selection import ParameterGrid
from helper import train_and_evaluate

# Define MPI message tags
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

def main():
    # Initializations and preliminaries 
    comm = MPI.COMM_WORLD           # get MPI communicator object
    size = comm.size                # total number of processes
    rank = comm.rank                # Rank of this process
    status = MPI.Status()           # get MPI status object
    scores = []
    tags = enum('READY', 'DONE', 'EXIT', 'START')
    triplets = np.load('100_triplets.npy')

    if rank == 0: 
        # Master process executes code below
        params = {'dm': [0, 1],
              'vector_size': [100, 200], 
              'corpus': ['numtoken']}
        tasks = list(ParameterGrid(params))
        task_index = 0
        num_workers = size - 1
        closed_workers = 0
        print('Master starting with %d workers' % num_workers)

        while closed_workers < num_workers:
            score = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
            source = status.Get_source()
            tag = status.Get_tag()
            if tag == tags.READY:
                # Worker is ready, so send it a task
                if task_index < len(tasks):
                    comm.send(tasks[task_index], dest=source, tag=tags.START)
                    print('Sending task %d to worker %d' % (task_index, source))
                    task_index += 1
                else:
                    comm.send(None, dest=source, tag=tags.EXIT)
            elif tag == tags.DONE:
                scores.append(score)
                with open('scores.txt', 'w+') as scores_file: #seems like it is ok w full scores, rewrites?
                    json.dump(scores, scores_file)
                print('Got data from worker %d' % source)
            elif tag == tags.EXIT:
                print('Worker %d exited.' % source)
                closed_workers += 1

            print('Master finishing')
    else:
        # Worker processes execute code below
        name = MPI.Get_processor_name()
        while True:
            comm.send(None, dest=0, tag=tags.READY)
            task = comm.recv(source=0, tag=MPI.ANY_TAG, status=status)
            tag = status.Get_tag()
            if tag == tags.START:
                # Do the work here
                score = train_and_evaluate(triplets, task)
                #score_formatted = {k: v for d in score for k, v in d.items()}
                comm.send(score, dest=0, tag=tags.DONE)
            elif tag == tags.EXIT:
                break

        comm.send(None, dest=0, tag=tags.EXIT)
    

if __name__ == '__main__':
    main()
    
    




