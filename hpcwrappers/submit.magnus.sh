#!/bin/sh

#sbatch --account=$IVEC_PROJECT --time=00:05:00 --nodes=4 --ntasks-per-node=1 -p debugq run.sh


for i in $(seq 1 -1 1)
do
	sbatch --account=$IVEC_PROJECT --time=00:05:00 --nodes=$i --ntasks-per-node=1 --dependency=singleton run.sh
done




