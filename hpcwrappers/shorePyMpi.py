import shore
import os
import sys
from mpi4py import MPI as mpi

comm = mpi.COMM_WORLD
rank = comm.Get_rank()
shore_root = os.environ.get('SHORE_ROOT')
local_shore_root = shore_root + '/mongo_node' + str(rank)
if not os.path.exists(local_shore_root):
    os.makedirs(local_shore_root)

mongod_cmd = 'numactl --interleave=all mongod --quiet --dbpath={0} &'.format(local_shore_root)
os.system(mongod_cmd)

shore.start_daemon()

sys.path.append(sys.argv[1])
import benchmark
benchmark.write_bench(shore)

shore.stop_daemon()

