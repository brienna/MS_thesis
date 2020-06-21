"""
To run this script, open Terminal window and type: ipcluster start --profile=ipy_profile &
Ensure that the profile name matches the one we're using below. 
Wait until 
Open another Terminal window, navigate to this directory, type: python script.py
To stop the engine type in a third Terminal window: ipcluster stop --profile=ipy_profile
Helpful resource: https://www.hyamani.eu/2018/05/20/parallel-super-computing-with-scikit-learn/
Issues where I can't update a module once I've used it in the engine, I have to rename it or reset the engine
"""

import os
import sys
import glob
import pickle
import logging
import argparse
import numpy as np
from joblib import delayed, cpu_count
from joblib import Parallel, parallel_backend, register_parallel_backend
from ipyparallel import Client
from ipyparallel.joblib import IPythonParallelBackend
from sklearn.model_selection import ParameterGrid
from timeit import default_timer as timer
from datetime import timedelta
from helper import train_and_evaluate # module in the same directory

# Get current directory
FILE_DIR = os.path.dirname(os.path.abspath('__file__'))
sys.path.append(FILE_DIR)

# Prepare the logger
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--profile", 
					default="ipy_profile", 
					help="Name of IPython profile to use")
args = parser.parse_args()
profile = args.profile
logging.basicConfig(filename=os.path.join(FILE_DIR,profile+'.log'),
					filemode='w',
					level=logging.DEBUG)
print("number of CPUs found: {0}".format(cpu_count()))
logging.info("number of CPUs found: {0}".format(cpu_count()))
logging.info("args.profile: {0}".format(profile))


# Prepare the engines
c = Client(profile=profile)
# Make sure that each engine is running in the right 
# working directory to access the custom function(s)
c[:].map(os.chdir, [FILE_DIR]*len(c))
logging.info("c.ids :{0}".format(str(c.ids)))
bview = c.load_balanced_view()
register_parallel_backend('ipyparallel', lambda : IPythonParallelBackend(view=bview))


# Get data and triplets (we want just the filenames of the preprocessed documents)
DATAPATH = os.path.join('/Volumes/BRIENNAKH/Thesis/data/2020_06_12_abstract_tokens/numtoken/*.npy')
data = np.array(glob.glob(DATAPATH))[:1000]
triplets = np.load('/Volumes/BRIENNAKH/Thesis/results/2020_06_19_doc2vec_1000_docs/100_triplets.npy')
logging.info('Number of documents: ' + str(len(data)))
logging.info('Number of triplets: ' + str(len(triplets)))

# Set parameters to test
params = {
    'dm': [0, 1],
    'vector_size': [100, 300]
}

# Run the code
start = timer()
with parallel_backend('ipyparallel'):
    scores = Parallel(n_jobs=len(c))(delayed(train_and_evaluate)(data, triplets, p, model_id) for model_id, p in enumerate(ParameterGrid(params)))
    scores_formatted = {k: v for d in scores for k, v in d.items()}
    with open('scores.pkl', 'wb') as f:
        pickle.dump(scores_formatted, f, pickle.HIGHEST_PROTOCOL)
end = timer()
logging.info("Execution time HH:MM:SS: {0}".format(timedelta(seconds=end-start)))



