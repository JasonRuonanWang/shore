#    (c) University of Western Australia
#    International Centre of Radio Astronomy Research
#    M468/35 Stirling Hwy
#    Perth WA 6009
#    Australia
#
#    Copyright by UWA,
#    All rights reserved
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston,
#    MA 02111-1307  USA
#
#    Any bugs, problems, and/or suggestions please email to
#    jason.wang@icrar.org or jason.ruonan.wang@gmail.com


import sys
sys.path.append('../')
import shoreClient
import numpy as np
import operator
import functools


shorePutCyDict = {}


cdef public void shoreZmqInitCy():
    shoreClient.shoreZmqInit()

cdef void shorePutScaler(const char *doid, const char* column, unsigned int rowid, unsigned int *shape_c, int dtype, const void *data_c):
    data = data_c[0]
    shoreClient.shorePut(doid, column, rowid, None, dtype, data)


cdef void shorePutArray(const char *doid, const char* column, unsigned int rowid, unsigned int *shape_c, int dtype, const void *data_c):
    cdef int shape_t
    cdef int[:] data
    shape = []
    for i in range(0, shape_c[0]):
        shape.append(shape_c[i+1])
    shape_t=functools.reduce(operator.mul, shape, 1)
    data = <int[:shape_t]>data_c
    data_np = np.asarray(data)
    data_np_rs = data_np.reshape(shape)
    shoreClient.shorePut(doid, column, rowid, shape, dtype, data)
    print data_c[0]
    print data[0]
    print data_np[0]
    print data_np_rs[0]


cdef public void shorePutCy(const char *doid, const char* column, unsigned int rowid, unsigned int *shape_c, int dtype, const void *data_c):
    if shape_c:
        shorePutArray(doid, column, rowid, shape_c, dtype, data_c)
    else:
        shorePutScaler(doid, column, rowid, shape_c, dtype, data_c)




