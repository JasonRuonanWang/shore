import numpy as np
import uuid
import random


def write_bench_one(shore, backend, rows, shape, datatype):

    print "write_bench_one"
    doid = str(uuid.uuid1())
    column = 'data_Float'
    for row in range(rows):
        print "write_bench"
        data = np.ndarray([1]+shape).astype(datatype)
        data.fill(3)
        shore.client.put(data, doid, column, row, 1, backend=backend)

def write_bench(shore):

    backends = ['hdf5', 'gridfs', 'mongo', 'adios']
    max_rows = 100
    max_array_dimensions = 3
    min_array_dimensions = 1
    max_array_dimension = 1000
    min_array_dimension = 100
    datatypes = [np.int8, np.uint8, np.int16, np.uint16, np.int32, np.uint32, np.float32, np.float64, np.complex64, np.complex128]

    iterations = 10

    for i in range(iterations):
#        try:
            backend = random.choice(backends)
            datatype = random.choice(datatypes)
            rows = random.randrange(0, max_rows)
            dimensions = random.randrange(min_array_dimensions, max_array_dimensions)
            shape = []
            for j in range(dimensions):
                dimension = random.randrange(min_array_dimension, max_array_dimension)
                shape.append(dimension)
            write_bench_one(shore, backend, rows, shape, datatype)
#        except:
#            pass



if __name__ == "__main__":
    write_bench()

