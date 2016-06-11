#!/bin/sh


for i in $(seq 1 -1 1)
do
	yhbatch -p free --time=02:00:00 --nodes=$i --ntasks-per-node=1 --dependency=singleton run.tianhe.sh
done




