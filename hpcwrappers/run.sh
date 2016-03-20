#!/bin/bash --login

if [ "$JOBSCHEDULER" == "slurm" ]; then
    JOBID=$SLURM_JOBID
    JOBDIR=$SLURM_SUBMIT_DIR
    RUN="aprun -B"
fi
if [ "$JOBSCHEDULER" == "pbs" ]; then
    JOBID=$PBS_JOBID
    JOBDIR=$PBS_O_WORKDIR
    RUN="mpirun"
fi

$RUN python $JOBDIR/shorePyMpi.py $JOBDIR


