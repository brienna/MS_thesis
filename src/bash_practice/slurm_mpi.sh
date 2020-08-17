#!/bin/bash -l

# NOTE the -l flag!

# This is an example job file for a multi-core MPI job.

# Note that all of the following statements below that begin

# with #SBATCH are actually commands to the SLURM scheduler

# Please copy this file to your home directory and modify it 

# to suit your needs.

#

# If you need any help,please email rc-help@rit.edu

#

# Name of the job - You'll probably want to customize this.

#SBATCH -J mpi_test

# Standard out and Standard Error output files

#SBATCH -o mpi_test.o

#SBATCH -e mpi_test.e

# To send emails, set the address below and remove one of the '#' sings

##SBATCH --mail-user=bkh4324@rit.edu

# notify on state change: BEGIN, END, FAIL, OR ALL

# 5 days is the run time MAX, anything over will be KILLED unless you talk with RC

# Request 4 days and 5 hours

#SBATCH -t 4-5:0:0

#Put the job in the appropriate partition matching the account and request FOUR cores

#SBATCH - A <account_name> -p <onboard, tier1, tier2, tier3> -n 4

#Job membory requirements in MB=m (default), GB=g, or TB=t

#SBATCH --mem=3g

#

# Your job script goes below this line.

#

echo "(${HOSTNAME}) sleeping for 1 minute to simulate work (ish)"

echo "(${HOSTNAME}) even though this script has claimed four cores"

echo "(${HOSTNAME}) ... it won't be using all "

sleep 60

echo "(${HOSTNAME}) Ahhh, alarm clock!"