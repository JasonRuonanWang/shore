import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient()
db = client.shore


def level2(x):
    s = 0.03125
    while s<x:
        s=s*2
    return s

def plot(para, xmin, xmax, ymin, ymax, filename):

    cursor = db.profiling.find()
    print cursor.count()
    MBytes_dict = {}
    s = 0
    for i in cursor:
        x = float(i['MBytes'])
        if x > xmin and x < xmax:
            y = float(i['MBps'])
            if y > ymin and y < ymax:
                if i['backend'] not in MBytes_dict:
                    MBytes_dict[i['backend']] = {}
                if i[para] not in MBytes_dict[i['backend']]:
                    MBytes_dict[i['backend']][i[para]] = {}
                if x not in MBytes_dict[i['backend']][i[para]]:
                    MBytes_dict[i['backend']][i[para]][x] = []
                MBytes_dict[i['backend']][i[para]][x].append(y)
                s = s+1
    print s

    cursor = db.profiling.find()
    print cursor.count()
    MBytes_ave = {}
    s = 0
    for i in cursor:
        x = float(i['MBytes'])
        if x > xmin and x < xmax:
            y = float(i['MBps'])
#            if y > ymin and y < ymax:
            if i['backend'] not in MBytes_ave:
                MBytes_ave[i['backend']] = {}
            x_top = level2(x)
            if x_top not in MBytes_ave[i['backend']]:
                MBytes_ave[i['backend']][x_top] = []
            MBytes_ave[i['backend']][x_top].append(y)
            s = s+1
    print s

    del MBytes_dict['adios']
    del MBytes_ave['adios']

    color = {'hdf5':'ro',
            'adios':'gx',
            'mongo':'bv',
            'gridfs':'y*'}
    color_line = {'hdf5':'r',
            'adios':'g',
            'mongo':'b',
            'gridfs':'y'}

    legend_handler = {}
    legend_handler_line = {}


    for i in MBytes_dict:
        for j in MBytes_dict[i]:
            for k in MBytes_dict[i][j]:
                handler, = plt.semilogx(k, sum(MBytes_dict[i][j][k])/len(MBytes_dict[i][j][k]), color[i], markersize=(j+3)*1.5)
                if j == 1:
                    legend_handler[i] = handler

    for i in MBytes_ave:
            for k in MBytes_ave[i]:
                handler, = plt.semilogx([k/2, k], [sum(MBytes_ave[i][k])/len(MBytes_ave[i][k]), sum(MBytes_ave[i][k])/len(MBytes_ave[i][k])], color_line[i], linewidth = 2 )
                legend_handler_line[i] = handler

    plt.xlabel('Size of data per write operation in Bytes')
    plt.ylabel('Write throughput of an individual process in MB/s')

    try:
        plt.legend([legend_handler['adios'], legend_handler['hdf5'], legend_handler['mongo'], legend_handler['gridfs'], legend_handler_line['adios'], legend_handler_line['hdf5'], legend_handler_line['mongo'], legend_handler_line['gridfs']] ,['ADIOS', 'HDF5', 'MongoDB', 'GridFS', 'ADIOS Average', 'HDF5 Average', 'MongoDB Average', 'GridFS Average'], loc=2)
    except:
        plt.legend([legend_handler['hdf5'], legend_handler['mongo'], legend_handler['gridfs'], legend_handler_line['hdf5'], legend_handler_line['mongo'], legend_handler_line['gridfs']] ,['HDF5', 'MongoDB', 'GridFS', 'HDF5 Average', 'MongoDB Average', 'GridFS Average'], loc=2)
    plt.savefig(filename+'.pdf', format='pdf', dpi=100)


plot('mpisize', 0.001, 100, 0, 1000, 'without_adios')


