#!/bin/bash 



source /HOME/ac_shao_tan_1/jason/bashrc 

while true; do
    mpirun python $SLURM_SUBMIT_DIR/shorePyMpi.py $SLURM_SUBMIT_DIR
done


