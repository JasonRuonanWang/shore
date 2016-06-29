import matplotlib.pyplot as plt
from pymongo import MongoClient
import math
import numpy as np

client = MongoClient()
db = client.shore


def level2(x):
    s = 0.03125
    while s<x:
        s=s*2
    return s

def plot(para):

    cursor = db.profiling.find()
    print cursor.count()
    MBytes_dict = {}
    s = 0
    for i in cursor:
        x = float(i['MBytes']) * 1000000
        y = float(i['MBps'])* 1000000
        if i['backend'] not in MBytes_dict:
            MBytes_dict[i['backend']] = {}
        if i[para] not in MBytes_dict[i['backend']]:
            MBytes_dict[i['backend']][i[para]] = {}
        if x not in MBytes_dict[i['backend']][i[para]]:
            MBytes_dict[i['backend']][i[para]][x] = []
        MBytes_dict[i['backend']][i[para]][x].append(y)
        s = s+1
    print s


    color = {'hdf5':'r+',
            'adios':'gx',
            'mongo':'bv',
            'gridfs':'y*'}

    legend_handler = {}

    for i in MBytes_dict:
        for j in MBytes_dict[i]:
            for k in MBytes_dict[i][j]:
                handler, = plt.loglog(k, sum(MBytes_dict[i][j][k])/len(MBytes_dict[i][j][k]), color[i], markersize=math.log(j, 2)+5, alpha = 0.6)
                if j == 1:
                    legend_handler[i] = handler


    plt.xlabel('Size of data per write operation in bytes')
    plt.ylabel('Write throughput of an individual process in bytes per second')

    plt.grid(True, which="both")
    try:
        plt.legend([legend_handler['adios'], legend_handler['hdf5'], legend_handler['mongo'], legend_handler['gridfs']] ,['ADIOS', 'HDF5', 'MongoDB', 'GridFS'], loc=2, fontsize=10)
    except:
        plt.legend([legend_handler['hdf5'], legend_handler['mongo'], legend_handler['gridfs']] ,['HDF5', 'MongoDB', 'GridFS'], loc=2, fontsize=10)
    plt.savefig('profiling_samples.pdf', format='pdf', dpi=100)

    plt.figure()

    cursor = db.profiling.find()
    print cursor.count()
    MBytes_ave = {}
    s = 0
    for i in cursor:
        x = float(i['MBytes'])* 1000000
        y = float(i['MBps'])* 1000000
        if i['backend'] not in MBytes_ave:
            MBytes_ave[i['backend']] = {}
        x_top = level2(x)
        if x_top not in MBytes_ave[i['backend']]:
            MBytes_ave[i['backend']][x_top] = []
        if y > 0:
            MBytes_ave[i['backend']][x_top].append(y)
            s = s+1
    print s

    color_line = {'hdf5':'r',
            'adios':'g',
            'mongo':'b',
            'gridfs':'y'}

    co_line = {'hdf5': 1.149,
            'adios': 1.320,
            'mongo': 1.516,
            'gridfs':1.741}

    legend_handler_line = {}

    for i in MBytes_ave:
        for k in MBytes_ave[i]:
            if len(MBytes_ave[i][k]) > 0:
                handler, = plt.loglog([k/2, k], [sum(MBytes_ave[i][k])/len(MBytes_ave[i][k]), sum(MBytes_ave[i][k])/len(MBytes_ave[i][k])], color_line[i], linewidth = 2)
                legend_handler_line[i] = handler
                maxn = np.percentile(MBytes_ave[i][k], 100)
                minn = np.percentile(MBytes_ave[i][k], 10)
                plt.vlines(k/co_line[i], minn , maxn, color_line[i])


    plt.xlabel('Size of data per write operation in bytes')
    plt.ylabel('Write throughput of an individual process in bytes per second')

    plt.grid(True, which="both")
    try:
        plt.legend([legend_handler_line['adios'], legend_handler_line['hdf5'], legend_handler_line['mongo'], legend_handler_line['gridfs']] ,['ADIOS Average', 'HDF5 Average', 'MongoDB Average', 'GridFS Average'], loc=2, fontsize=10)
    except:
        plt.legend([legend_handler_line['hdf5'], legend_handler_line['mongo'], legend_handler_line['gridfs']] ,['HDF5 Average', 'MongoDB Average', 'GridFS Average'], loc=2, fontsize=10)
    plt.savefig('profiling_average.pdf', format='pdf', dpi=100)

plot('mpisize')


