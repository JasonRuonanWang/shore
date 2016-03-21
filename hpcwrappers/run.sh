#!/bin/bash --login

PYTHON="/home/jwang/pyenv/bin/python"

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

$RUN $PYTHON $JOBDIR/shorePyMpi.py $JOBDIR


