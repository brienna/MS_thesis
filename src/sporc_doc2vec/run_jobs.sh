#!/bin/bash -l

# NOTE the -l flag! https://stackoverflow.com/questions/20499596/bash-shebang-option-l

# This is an example job file for a multi-core MPI job.

# Note that all of the following statements below that begin

# with #SBATCH are actually commands to the SLURM scheduler

# Please copy this file to your home directory and modify it 

# to suit your needs.

#

# If you need any help,please email rc-help@rit.edu

#

# Name of the job.

#SBATCH -J doc2vec_abstracts

# Standard out and Standard Error output files

#SBATCH -o doc2vec_abstracts.o

#SBATCH -e doc2vec_abstracts.e

# To send emails, set the address below and remove one of the '#' sings

##SBATCH --mail-user=bkh4324@rit.edu

# notify on state change: BEGIN, END, FAIL, OR ALL

#SBATCH --mail-type=ALL

# 5 days is the run time MAX, anything over will be KILLED unless you talk with RC

# Request 4 days and 5 hours

#SBATCH -t 2:0:0

#Put the job in the appropriate partition matching the account and request cores (check parameter grid for how many)

#SBATCH -A avxiv -p debug --ntasks=20

#Job membory requirements in MB=m (default), GB=g, or TB=t

#SBATCH --mem=100g

######################################################################

# Load modules
spack load py-gensim
spack load py-mpi4py
spack load py-scikit-learn

# Run 
srun -n $SLURM_NTASKS --mpi=pmix_v3 python script.py 

# IN TERMINAL NAVIGATE TO DIR W/ THIS .SH FILE & TYPE sbatch start_script.sh script.py
# CHECK WHERE IT IS IN THE QUEUE WITH queue -u bkh4324
# maybe cuz of the -l flag it won't work, need to check


