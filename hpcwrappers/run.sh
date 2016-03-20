#!/bin/bash --login

QUOTA="5000000000" # in KB
OUTPUT="$SHORE_ROOT"

if [ "$JOBSCHEDULER" == "slurm" ]; then
    JOBID=$SLURM_JOBID
    JOBDIR=$SLURM_SUBMIT_DIR
fi

if [ "$JOBSCHEDULER" == "pbs" ]; then
    JOBID=$PBS_JOBID
    JOBDIR=$PBS_O_WORKDIR
fi

for i in $(seq 1 10)
do
    for rows in $(seq 100 100 1000)
    do
        for length in $(seq 1000 1000 20000)
        do
            CHECK=$(du -s $OUTPUT | cut -f1)
            if [ "$CHECK" -gt "$QUOTA" ]; then
                echo "$CHECK bytes in $OUTPUT, reaching disk quota $QUOTA, cleaning up ..."
                mongo shore --eval 'db.data.remove({})'
            fi

            if [ "$JOBSCHEDULER" == "slurm" ]; then
                RUN="aprun -B"
            fi

            if [ "$JOBSCHEDULER" == "pbs" ]; then
                RUN="mpirun"
            fi

            RUNLINE="$RUN python $JOBDIR/shorePyMpi.py"
            echo $RUNLINE
            $RUNLINE
        done
    done
done

