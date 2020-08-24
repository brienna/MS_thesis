# github.com/jbornschein/mpi4py-examples/blob/master/09-task-pull.py

# mpirun -np 5 python script.py

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
import os 
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
    tags = enum('READY', 'DONE', 'EXIT', 'START')
    triplets = np.load('20000_triplets.npy')
    params = {'dm': [0, 1],
              'vector_size': [100, 500, 1000, 2500, 5000, 7500, 10000], 
              'corpus': ['abstracts/basic_preprocessing',
                         'abstracts/and_stemming',
                         'abstracts/and_lemmatization',
                         'abstracts/and_stopword_removal',
                         'fulltexts/basic_preprocessing',
                         'fulltexts/and_stemming',
                         'fulltexts/and_lemmatization',
                         'fulltexts/and_stopword_removal'],
              'epochs': [10, 25, 50, 100],
              'window': [2, 5, 10, 20],
              'hs': [0, 1],
              'min_count': [2, 5, 10, 20]}
    tasks = list(ParameterGrid(params))
    # Collect scores and remove any tasks that have been completed
    if os.path.exists('scores.txt'):
        with open('scores.txt', 'r') as sfile:
            scores = json.load(sfile)
            tasks = [x for x in list(ParameterGrid(params)) if x not in [x['parameters'] for x in scores]]
    else:
        scores = []
    
    task_index = 0
    num_workers = size - 1
    closed_workers = 0

    if rank == 0: 
        # Master process executes code below
        print('Master starting with %d workers' % num_workers)

        while closed_workers < num_workers:
            score = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status) 
            source = status.Get_source()
            tag = status.Get_tag()
            if tag == tags.READY:
                if task_index < len(tasks): # Worker is ready, so send it a task
                    print('Sending task %d to worker %d' % (task_index, source))
                    comm.send(tasks[task_index], dest=source, tag=tags.START)
                    task_index += 1
                else:
                    comm.send(None, dest=source, tag=tags.EXIT) # No more tasks? Tell worker to exit
            elif tag == tags.DONE:
                print('Worker ' + str(source) + ' has completed, writing model score...')
                scores.append(score)
                with open('scores.txt', 'w+') as sfile: # dump all scores anew
                    json.dump(scores, sfile)
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
                print('Training model with parameters: ' + str(task))
                score = train_and_evaluate(triplets, task)
                comm.send(score, dest=0, tag=tags.DONE)
            elif tag == tags.EXIT:
                break

        comm.send(None, dest=0, tag=tags.EXIT)
    

if __name__ == '__main__':
    main()
    
    




