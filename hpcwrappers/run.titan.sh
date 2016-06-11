#!/bin/bash


cd $PBS_O_WORKDIR

#while true; do
    aprun /lustre/atlas2/csc143/proj-shared/ska/lib/python/bin/python $PBS_O_WORKDIR/shorePyMpi.py $PBS_O_WORKDIR
#done


