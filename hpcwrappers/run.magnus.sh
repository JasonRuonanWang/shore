#!/bin/bash --login

PYTHON="/home/jwang/pyenv27/bin/python"

. /home/jwang/pyenv27/bin/activate

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

#while true; do
    $RUN $PYTHON $JOBDIR/shorePyMpi.py $JOBDIR
#done


