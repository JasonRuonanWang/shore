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


cdef public void shoreZmqInitCy():
    shoreClient.shoreZmqInit()

cdef public void shorePutCy(const char *doid, const char* column, unsigned int rowid, unsigned int *shape_c, void *data_c):
    shape = []
    for i in range(0, shape_c[0]):
        shape.append(shape_c[i+1])
    cdef int shape_t=functools.reduce(operator.mul, shape, 1)


    cdef int[:] data = <int[:shape_t]>data_c
#    my_array_np = np.asarray(my_array)
#    my_array_np_rs = my_array_np.reshape(shape)


    shoreClient.shorePut(doid, column, rowid, shape, data)





