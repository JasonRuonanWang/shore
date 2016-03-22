from shoreClient import shoreClient as shore
import numpy as np
import sys
import uuid



def write_bench():


    for backend in ['hdf5', 'gridfs', 'mongo']:

        doid = str(uuid.uuid1())
        column = 'data_Float'
        rows = 10
        for row in range(rows):

            xdim = 1024
            ydim = 256
            data = np.ndarray([1,xdim,ydim]).astype(np.float32)
            for x in range(xdim):
                for y in range(ydim):
                    data[0][x][y] = x * 100 + y
            shore.shorePut(data, doid, column, row, 1, backend=backend)


if __name__ == "__main__":
    write_bench()

