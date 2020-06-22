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

# 5 days is the run time MAX, anything over will be KILLED unless you talk with RC

# Request 4 days and 5 hours

#SBATCH -t 4-5:0:0

#Put the job in the appropriate partition matching the account and request cores

#SBATCH - A avxiv -p tier1 --ntasks=16

#Job membory requirements in MB=m (default), GB=g, or TB=t

#SBATCH --mem=100g

######################################################################

# Delete all ipython profiles older than 1 day.
find ~/.ipython/profile_job* -maxdepth 0 -type d -ctime +1 | xargs rm -r

# Create a new ipython profile appended with the job id number
profile=job_${SLURM_JOB_ID}
echo "Creating profile_${profile}"
$HOME/conda/bin/ipython profile create ${profile}
$HOME/conda/bin/ipcontroller --ip="*" --profile=${profile} &
sleep 10

# Run ipengine on each available core
srun $HOME/conda/bin/ipengine --profile=${profile} --location=$(hostname) &
sleep 25

echo "Launching job for script $1"
$HOME/conda/bin/python $1 -p ${profile}

# IN TERMINAL NAVIGATE TO DIR W/ THIS .SH FILE & TYPE sbatch start_script.sh script.py
# CHECK WHERE IT IS IN THE QUEUE WITH queue -u bkh4324
# maybe cuz of the -l flag it won't work, need to check


