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
from shoreClient import shoreClient
import numpy as np
cimport numpy as np
from libcpp cimport bool
from libc.string cimport memcpy

cdef extern from "stdbool.h":
    pass

cdef void shorePutCyBool(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef bool[:] data_mv = <bool[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape([rows]+shape)
    shoreClient.shorePut(data, doid, column, rowid, rows)
cdef void shorePutCyChar(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef char[:] data_mv = <char[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape([rows]+shape).astype('int8')
    shoreClient.shorePut(data, doid, column, rowid, rows)
cdef void shorePutCyUChar(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef unsigned char[:] data_mv = <unsigned char[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape([rows]+shape)
    shoreClient.shorePut(data, doid, column, rowid, rows)
cdef void shorePutCyShort(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef short[:] data_mv = <short[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape([rows]+shape)
    shoreClient.shorePut(data, doid, column, rowid, rows)
cdef void shorePutCyUShort(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef unsigned short[:] data_mv = <unsigned short[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape([rows]+shape)
    shoreClient.shorePut(data, doid, column, rowid, rows)
cdef void shorePutCyInt(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef int[:] data_mv = <int[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape([rows]+shape)
    shoreClient.shorePut(data, doid, column, rowid, rows)
cdef void shorePutCyUInt(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef unsigned int[:] data_mv = <unsigned int[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape([rows]+shape)
    shoreClient.shorePut(data, doid, column, rowid, rows)
cdef void shorePutCyFloat(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef float[:] data_mv = <float[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape([rows]+shape)
    shoreClient.shorePut(data, doid, column, rowid, rows)
cdef void shorePutCyDouble(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef double[:] data_mv = <double[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape([rows]+shape)
    shoreClient.shorePut(data, doid, column, rowid, rows)
cdef void shorePutCyComplex(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef float complex[:] data_mv = <float complex[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape([rows]+shape)
    shoreClient.shorePut(data, doid, column, rowid, rows)
cdef void shorePutCyDComplex(const char *doid, const char* column, unsigned int rowid, unsigned int rows, list shape, const void *data_c, int nelements):
    cdef double complex[:] data_mv = <double complex[:nelements]>data_c
    data = np.ascontiguousarray(data_mv).reshape([rows]+shape)
    shoreClient.shorePut(data, doid, column, rowid, rows)


cdef public int shorePutCy(const char *doid, const char* column, const unsigned int rowid, const unsigned int rows, const unsigned int *shape_c, const int dtype, const void *data_c):
    shape = []
    for i in range(0, shape_c[0]):
        shape.append(shape_c[i+1])
    nelements = rows
    for x in shape:
        nelements *= x

    if dtype == 0:
        shorePutCyBool(doid, column, rowid, rows, shape, data_c, nelements)
    elif dtype == 1:
        shorePutCyChar(doid, column, rowid, rows, shape, data_c, nelements)
    elif dtype == 2:
        shorePutCyUChar(doid, column, rowid, rows, shape, data_c, nelements)
    elif dtype == 3:
        shorePutCyShort(doid, column, rowid, rows, shape, data_c, nelements)
    elif dtype == 4:
        shorePutCyUShort(doid, column, rowid, rows, shape, data_c, nelements)
    elif dtype == 5:
        shorePutCyInt(doid, column, rowid, rows, shape, data_c, nelements)
    elif dtype == 6:
        shorePutCyUInt(doid, column, rowid, rows, shape, data_c, nelements)
    elif dtype == 7:
        shorePutCyFloat(doid, column, rowid, rows, shape, data_c, nelements)
    elif dtype == 8:
        shorePutCyDouble(doid, column, rowid, rows, shape, data_c, nelements)
    elif dtype == 9:
        shorePutCyComplex(doid, column, rowid, rows, shape, data_c, nelements)
    elif dtype == 10:
        shorePutCyDComplex(doid, column, rowid, rows, shape, data_c, nelements)

    return 0

cdef void shoreGetChar(np.ndarray data_ret, int nelements, void *data_c):
    cdef np.ndarray[char, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(data_ret,[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(char) * nelements)
cdef void shoreGetUchar(np.ndarray data_ret, int nelements, void *data_c):
    cdef np.ndarray[unsigned char, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(data_ret,[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(unsigned char) * nelements)
cdef void shoreGetShort(np.ndarray data_ret, int nelements, void *data_c):
    cdef np.ndarray[short, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(data_ret,[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(short) * nelements)
cdef void shoreGetUshort(np.ndarray data_ret, int nelements, void *data_c):
    cdef np.ndarray[unsigned short, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(data_ret,[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(unsigned short) * nelements)
cdef void shoreGetInt(np.ndarray data_ret, int nelements, void *data_c):
    cdef np.ndarray[int, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(data_ret,[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(int) * nelements)
cdef void shoreGetUint(np.ndarray data_ret, int nelements, void *data_c):
    cdef np.ndarray[unsigned int, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(data_ret,[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(unsigned int) * nelements)
cdef void shoreGetFloat(np.ndarray data_ret, int nelements, void *data_c):
    cdef np.ndarray[float, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(data_ret,[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(float) * nelements)
cdef void shoreGetDouble(np.ndarray data_ret, int nelements, void *data_c):
    cdef np.ndarray[double, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(data_ret,[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(double) * nelements)
cdef void shoreGetComplex(np.ndarray data_ret, int nelements, void *data_c):
    cdef np.ndarray[float complex, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(data_ret,[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(float complex) * nelements)
cdef void shoreGetDcomplex(np.ndarray data_ret, int nelements, void *data_c):
    cdef np.ndarray[double complex, ndim=1, mode="c"] data = np.ascontiguousarray( np.reshape(data_ret,[nelements]) )
    memcpy(data_c, <const void*> data.data, sizeof(double complex) * nelements)

cdef public int shoreGetCy(const char *doid, const char* column, const unsigned int rowid, const unsigned int rows, void *data_c):
    ret = shoreClient.shoreGet(doid, column, rowid, rows)
    if ret is None:
        return -1

    dtype = ret.dtype
    shape = ret.shape

    nelements = rows
    for x in shape:
        nelements *= x

    if dtype == 'int8':
        shoreGetChar(ret, nelements, data_c)
    elif dtype == 'uint8':
        shoreGetUchar(ret, nelements, data_c)
    elif dtype == 'int16':
        shoreGetShort(ret, nelements, data_c)
    elif dtype == 'uint16':
        shoreGetUshort(ret, nelements, data_c)
    elif dtype == 'int32':
        shoreGetInt(ret, nelements, data_c)
    elif dtype == 'uint32':
        shoreGetUint(ret, nelements, data_c)
    elif dtype == 'float32':
        shoreGetFloat(ret, nelements, data_c)
    elif dtype == 'float64':
        shoreGetDouble(ret, nelements, data_c)
    elif dtype == 'complex64':
        shoreGetComplex(ret, nelements, data_c)
    elif dtype == 'complex128':
        shoreGetDcomplex(ret, nelements, data_c)

    return 0


cdef public int shoreQueryCy(const char *doid, const char* column, unsigned int *rows, unsigned int *shape_c, int *dtype_c):
    ##### call python shoreClient
    ret = shoreClient.shoreQuery(doid, column)
    ##### shape

    if ret is None:
        return -1

    shape = ret['return']['column']['shape']
    shape_c[0]=len(shape)
    s = 1
    for i in shape:
        shape_c[s] = i
        s+=1
    ##### dtype
    dtype = ret['return']['column']['datatype']
    rows[0] = ret['return']['do']['total_rows']

    return 0

cdef public void shoreZmqInitCy():
    shoreClient.shoreZmqInit()


