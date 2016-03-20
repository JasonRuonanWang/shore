from shoreClient import shoreClient as shore
import numpy as np
import sys


def bench():

    doid = 'aaa'
    column = 'data_Float'
    row = 0
    rows = 10

    if len(sys.argv) > 1:
        doid = sys.argv[1]
        if len(sys.argv) > 2:
            column = sys.argv[2]
            if len(sys.argv) > 3:
                row = int(sys.argv[3])
                if len(sys.argv) > 4:
                    rows = int(sys.argv[4])

    xdim = 5
    ydim = 10
    data = np.ndarray([rows,xdim,ydim])
    for r in range(rows):
        for x in range(xdim):
            for y in range(ydim):
                data[r][x][y] = x * 100 + y

    ret = shore.shorePut(doid, column, row, data, rows)

