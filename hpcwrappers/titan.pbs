#!/bin/sh
#PBS -A csc143
#PBS -l walltime=02:00:00
#PBS -l nodes=1

cd $PBS_O_WORKDIR

while true; do
    aprun -n 1 -N 1 /lustre/atlas2/csc143/proj-shared/ska/lib/python/bin/python $PBS_O_WORKDIR/shorePyMpi.py $PBS_O_WORKDIR
done



