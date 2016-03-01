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
from libcpp cimport bool

shoreDataType = {
    0:'bool',
    1:'char',
    2:'uChar',
    3:'short',
    4:'uShort',
    5:'int',
    6:'uInt',
    7:'float',
    8:'double',
    9:'Complex',
    10:'DComplex'}

cdef extern from "stdbool.h":
    pass

cdef void shorePutArrayBool(const char *doid, const char* column, unsigned int rowid, list shape, int dtype, const void *data_c, int nelements):
    cdef bool[:] data = <bool[:nelements]>data_c
    shoreClient.shorePut(doid, column, rowid, shape, dtype, data)
cdef void shorePutArrayChar(const char *doid, const char* column, unsigned int rowid, list shape, int dtype, const void *data_c, int nelements):
    cdef char[:] data = <char[:nelements]>data_c
    shoreClient.shorePut(doid, column, rowid, shape, dtype, data)
cdef void shorePutArrayUChar(const char *doid, const char* column, unsigned int rowid, list shape, int dtype, const void *data_c, int nelements):
    cdef unsigned char[:] data = <unsigned char[:nelements]>data_c
    shoreClient.shorePut(doid, column, rowid, shape, dtype, data)
cdef void shorePutArrayShort(const char *doid, const char* column, unsigned int rowid, list shape, int dtype, const void *data_c, int nelements):
    cdef short[:] data = <short[:nelements]>data_c
    shoreClient.shorePut(doid, column, rowid, shape, dtype, data)
cdef void shorePutArrayUShort(const char *doid, const char* column, unsigned int rowid, list shape, int dtype, const void *data_c, int nelements):
    cdef unsigned short[:] data = <unsigned short[:nelements]>data_c
    shoreClient.shorePut(doid, column, rowid, shape, dtype, data)
cdef void shorePutArrayInt(const char *doid, const char* column, unsigned int rowid, list shape, int dtype, const void *data_c, int nelements):
    cdef int[:] data = <int[:nelements]>data_c
    shoreClient.shorePut(doid, column, rowid, shape, dtype, data)
cdef void shorePutArrayUInt(const char *doid, const char* column, unsigned int rowid, list shape, int dtype, const void *data_c, int nelements):
    cdef unsigned int[:] data = <unsigned int[:nelements]>data_c
    shoreClient.shorePut(doid, column, rowid, shape, dtype, data)
cdef void shorePutArrayFloat(const char *doid, const char* column, unsigned int rowid, list shape, int dtype, const void *data_c, int nelements):
    cdef float[:] data = <float[:nelements]>data_c
    shoreClient.shorePut(doid, column, rowid, shape, dtype, data)
cdef void shorePutArrayDouble(const char *doid, const char* column, unsigned int rowid, list shape, int dtype, const void *data_c, int nelements):
    cdef double[:] data = <double[:nelements]>data_c
    shoreClient.shorePut(doid, column, rowid, shape, dtype, data)
cdef void shorePutArrayComplex(const char *doid, const char* column, unsigned int rowid, list shape, int dtype, const void *data_c, int nelements):
    cdef float complex[:] data = <float complex[:nelements]>data_c
    shoreClient.shorePut(doid, column, rowid, shape, dtype, data)
cdef void shorePutArrayDComplex(const char *doid, const char* column, unsigned int rowid, list shape, int dtype, const void *data_c, int nelements):
    cdef double complex[:] data = <double complex[:nelements]>data_c
    shoreClient.shorePut(doid, column, rowid, shape, dtype, data)


cdef void shorePutArray(const char *doid, const char* column, const unsigned int rowid, const unsigned int *shape_c, const int dtype, const void *data_c):
    cdef int nelements
    shape = []
    for i in range(0, shape_c[0]):
        shape.append(shape_c[i+1])
    nelements = functools.reduce(operator.mul, shape, 1)
    if shoreDataType[dtype] == 'bool':
        shorePutArrayBool(doid, column, rowid, shape, dtype, data_c, nelements)
    elif shoreDataType[dtype] == 'char':
        shorePutArrayChar(doid, column, rowid, shape, dtype, data_c, nelements)
    elif shoreDataType[dtype] == 'uChar':
        shorePutArrayUChar(doid, column, rowid, shape, dtype, data_c, nelements)
    elif shoreDataType[dtype] == 'short':
        shorePutArrayShort(doid, column, rowid, shape, dtype, data_c, nelements)
    elif shoreDataType[dtype] == 'uShort':
        shorePutArrayUShort(doid, column, rowid, shape, dtype, data_c, nelements)
    elif shoreDataType[dtype] == 'int':
        shorePutArrayInt(doid, column, rowid, shape, dtype, data_c, nelements)
    elif shoreDataType[dtype] == 'uInt':
        shorePutArrayUInt(doid, column, rowid, shape, dtype, data_c, nelements)
    elif shoreDataType[dtype] == 'float':
        shorePutArrayFloat(doid, column, rowid, shape, dtype, data_c, nelements)
    elif shoreDataType[dtype] == 'double':
        shorePutArrayDouble(doid, column, rowid, shape, dtype, data_c, nelements)
    elif shoreDataType[dtype] == 'Complex':
        shorePutArrayComplex(doid, column, rowid, shape, dtype, data_c, nelements)
    elif shoreDataType[dtype] == 'DComplex':
        shorePutArrayDComplex(doid, column, rowid, shape, dtype, data_c, nelements)

cdef void shorePutScalar(const char *doid, const char* column, const unsigned int rowid, const unsigned int *shape_c, const int dtype, const void *data_c):
    data = data_c[0]
    shoreClient.shorePut(doid, column, rowid, None, dtype, data)

cdef public void shorePutCy(const char *doid, const char* column, const unsigned int rowid, const unsigned int *shape_c, const int dtype, const void *data_c):
    if shape_c:  #if array
        shorePutArray(doid, column, rowid, shape_c, dtype, data_c)
    else:        #if scalar
        shorePutScalar(doid, column, rowid, shape_c, dtype, data_c)


cdef public void shoreGetCy(const char *doid, const char* column, const unsigned int rowid, unsigned int *shape_c, int *dtype, void *data_c):
    shoreClient.shoreGet()

cdef public void shoreZmqInitCy():
    shoreClient.shoreZmqInit()


