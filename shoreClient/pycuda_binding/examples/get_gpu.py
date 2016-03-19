from shoreClient.pycuda_binding import shoreClientCuda as shore
import sys

doid = 'aaa'
column = 'data_Float'
row = 0
rows = 1

if len(sys.argv) > 1:
    doid = sys.argv[1]
    if len(sys.argv) > 2:
        column = sys.argv[2]
        if len(sys.argv) > 3:
            row = sys.argv[3]
            if len(sys.argv) > 4:
                rows = sys.argv[4]

ret=shore.shoreGet(doid,column,int(row),int(rows))
print ret

