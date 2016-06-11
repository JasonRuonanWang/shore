#!/bin/sh


for i in $(seq 1 -1 1)
do
    qsub -A csc143 -l walltime=00:05:00,nodes=1 run.titan.sh
done




