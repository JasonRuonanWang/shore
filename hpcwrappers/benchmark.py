from shoreClient import shoreClient as shore
import numpy as np
import sys
from mpi4py import MPI as mpi


def write_bench():

    comm = mpi.COMM_WORLD
    rank = comm.Get_rank()
    doid = 'write_bench_rank{0}'.format(rank)
    column = 'data_Float'
    rows = 10

    for row in range(rows):

        xdim = 1024
        ydim = 256
        data = np.ndarray([1,xdim,ydim]).astype(np.float32)
        for x in range(xdim):
            for y in range(ydim):
                data[0][x][y] = x * 100 + y
        shore.shorePut(doid, column, row, data, 1)


if __name__ == "__main__":
    write_bench()

