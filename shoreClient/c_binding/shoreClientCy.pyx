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

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

import sys
sys.path.append('../')
import shoreClient
import numpy as np
cimport numpy as np
np.get_include()
import operator
import functools
from libcpp cimport bool
from libc.string cimport memcpy
import ctypes

shoreDataType = {
    0:'bool',
    1:'char',
    2:'uchar',
    3:'short',
    4:'ushort',
    5:'int',
    6:'uint',
    7:'float',
    8:'double',
    9:'complex',
    10:'dcomplex'}

cdef extern from "stdbool.h":
    pass

cdef void shorePutCyBool(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef bool[:] data_mv = <bool[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape(shape)
    shoreClient.shorePut(doid, column, rowid, data, rows)
cdef void shorePutCyChar(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef char[:] data_mv = <char[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape(shape)
    shoreClient.shorePut(doid, column, rowid, data, rows)
cdef void shorePutCyUChar(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef unsigned char[:] data_mv = <unsigned char[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape(shape)
    shoreClient.shorePut(doid, column, rowid, data, rows)
cdef void shorePutCyShort(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef short[:] data_mv = <short[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape(shape)
    shoreClient.shorePut(doid, column, rowid, data, rows)
cdef void shorePutCyUShort(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef unsigned short[:] data_mv = <unsigned short[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape(shape)
    shoreClient.shorePut(doid, column, rowid, data, rows)
cdef void shorePutCyInt(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef int[:] data_mv = <int[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape(shape)
    shoreClient.shorePut(doid, column, rowid, data, rows)
cdef void shorePutCyUInt(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef unsigned int[:] data_mv = <unsigned int[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape(shape)
    shoreClient.shorePut(doid, column, rowid, data, rows)
cdef void shorePutCyFloat(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef float[:] data_mv = <float[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape(shape)
    shoreClient.shorePut(doid, column, rowid, data, rows)
cdef void shorePutCyDouble(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef double[:] data_mv = <double[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape(shape)
    shoreClient.shorePut(doid, column, rowid, data, rows)
cdef void shorePutCyComplex(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef float complex[:] data_mv = <float complex[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape(shape)
    shoreClient.shorePut(doid, column, rowid, data, rows)
cdef void shorePutCyDComplex(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef double complex[:] data_mv = <double complex[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape(shape)
    shoreClient.shorePut(doid, column, rowid, data, rows)


cdef public void shorePutCy(const char *doid, const char* column, const unsigned int rowid, const unsigned int rows, const unsigned int *shape_c, const int dtype, const void *data_c):
    shape = []
    for i in range(0, shape_c[0]):
        shape.append(shape_c[i+1])
    nelements = functools.reduce(operator.mul, shape, 1)
    if shoreDataType[dtype] == 'bool':
        shorePutCyBool(doid, column, rowid, rows, shape, data_c, nelements)
    elif shoreDataType[dtype] == 'char':
        shorePutCyChar(doid, column, rowid, rows, shape, data_c, nelements)
    elif shoreDataType[dtype] == 'uchar':
        shorePutCyUChar(doid, column, rowid, rows, shape, data_c, nelements)
    elif shoreDataType[dtype] == 'short':
        shorePutCyShort(doid, column, rowid, rows, shape, data_c, nelements)
    elif shoreDataType[dtype] == 'ushort':
        shorePutCyUShort(doid, column, rowid, rows, shape, data_c, nelements)
    elif shoreDataType[dtype] == 'int':
        shorePutCyInt(doid, column, rowid, rows, shape, data_c, nelements)
    elif shoreDataType[dtype] == 'uint':
        shorePutCyUInt(doid, column, rowid, rows, shape, data_c, nelements)
    elif shoreDataType[dtype] == 'float':
        shorePutCyFloat(doid, column, rowid, rows, shape, data_c, nelements)
    elif shoreDataType[dtype] == 'double':
        shorePutCyDouble(doid, column, rowid, rows, shape, data_c, nelements)
    elif shoreDataType[dtype] == 'complex':
        shorePutCyComplex(doid, column, rowid, rows, shape, data_c, nelements)
    elif shoreDataType[dtype] == 'dcomplex':
        shorePutCyDComplex(doid, column, rowid, rows, shape, data_c, nelements)


cdef void shoreGetBool(dict ret, int nelements, void *data_c):
    data_python = ret['data']
    data_python_reshaped = np.reshape(ret['data'],[nelements])
    data_python_retyped = data_python_reshaped.astype(np.uint8)
    cdef np.ndarray[unsigned char, ndim=1, mode="c"] data = np.ascontiguousarray(data_python_retyped)
    memcpy(data_c, <const void*> data.data, sizeof(unsigned char) * nelements)
cdef void shoreGetChar(dict ret, int nelements, void *data_c):
    cdef np.ndarray[char, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(ret['data'],[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(char) * nelements)
cdef void shoreGetUchar(dict ret, int nelements, void *data_c):
    cdef np.ndarray[unsigned char, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(ret['data'],[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(unsigned char) * nelements)
cdef void shoreGetShort(dict ret, int nelements, void *data_c):
    cdef np.ndarray[short, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(ret['data'],[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(short) * nelements)
cdef void shoreGetUshort(dict ret, int nelements, void *data_c):
    cdef np.ndarray[unsigned short, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(ret['data'],[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(unsigned short) * nelements)
cdef void shoreGetInt(dict ret, int nelements, void *data_c):
    cdef np.ndarray[int, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(ret['data'],[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(int) * nelements)
cdef void shoreGetUint(dict ret, int nelements, void *data_c):
    cdef np.ndarray[unsigned int, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(ret['data'],[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(unsigned int) * nelements)
cdef void shoreGetFloat(dict ret, int nelements, void *data_c):
    cdef np.ndarray[float, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(ret['data'],[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(float) * nelements)
cdef void shoreGetDouble(dict ret, int nelements, void *data_c):
    cdef np.ndarray[double, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(ret['data'],[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(double) * nelements)
cdef void shoreGetComplex(dict ret, int nelements, void *data_c):
    cdef np.ndarray[float complex, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(ret['data'],[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(float complex) * nelements)
cdef void shoreGetDcomplex(dict ret, int nelements, void *data_c):
    cdef np.ndarray[double complex, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(ret['data'],[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(double complex) * nelements)

cdef public void shoreGetCy(const char *doid, const char* column, const unsigned int rowid, const unsigned int rows, unsigned int *shape_c, int *dtype_c, void *data_c):
    ret = shoreClient.shoreGet(doid, column, rowid)
    dtype = ret['return']['column']['datatype']
    shape = [rows] + ret['return']['column']['shape']
    nelements = functools.reduce(operator.mul, shape, 1)
    if shoreDataType[dtype] == 'bool':
        shoreGetBool(ret, nelements, data_c)
    elif shoreDataType[dtype] == 'char':
        shoreGetChar(ret, nelements, data_c)
    elif shoreDataType[dtype] == 'uchar':
        shoreGetUchar(ret, nelements, data_c)
    elif shoreDataType[dtype] == 'short':
        shoreGetShort(ret, nelements, data_c)
    elif shoreDataType[dtype] == 'ushort':
        shoreGetUshort(ret, nelements, data_c)
    elif shoreDataType[dtype] == 'int':
        shoreGetInt(ret, nelements, data_c)
    elif shoreDataType[dtype] == 'uint':
        shoreGetUint(ret, nelements, data_c)
    elif shoreDataType[dtype] == 'float':
        shoreGetFloat(ret, nelements, data_c)
    elif shoreDataType[dtype] == 'double':
        shoreGetDouble(ret, nelements, data_c)
    elif shoreDataType[dtype] == 'complex':
        shoreGetComplex(ret, nelements, data_c)
    elif shoreDataType[dtype] == 'dcomplex':
        shoreGetDcomplex(ret, nelements, data_c)


cdef public int shoreQueryCy(const char *doid, const char* column, const unsigned int rowid, unsigned int *shape_c, int *dtype_c):
    ##### call python shoreClient
    ret = shoreClient.shoreQuery(doid, column)
    ##### shape
    shape = ret['return']['column']['shape']
    shape_c[0]=len(shape)
    s = 1
    for i in shape:
        shape_c[s] = i
        s+=1
    ##### dtype
    dtype = ret['return']['column']['datatype']
    dtype_c[0] = dtype
    return 0

cdef public void shoreZmqInitCy():
    shoreClient.shoreZmqInit()


