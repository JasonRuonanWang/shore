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


from files import files
import adios as ad
import numpy as np
import copy


class files_adios(files):

    def __init__(self, event, config):
        files.__init__(self, event, config)
        self.buffersize = 512
        self.maxrows = 10000
        self.dtype_numpy2adios = {
            np.dtype(np.int8)   : ad.DATATYPE.byte,
            np.dtype(np.uint8)  : ad.DATATYPE.unsigned_byte,
            np.dtype(np.int16)  : ad.DATATYPE.short,
            np.dtype(np.uint16) : ad.DATATYPE.unsigned_short,
            np.dtype(np.int32)  : ad.DATATYPE.integer,
            np.dtype(np.uint32) : ad.DATATYPE.unsigned_integer,
            np.dtype(np.int64)  : ad.DATATYPE.long,
            np.dtype(np.uint64) : ad.DATATYPE.unsigned_long,
            np.dtype(np.float32): ad.DATATYPE.real,
            np.dtype(np.float64): ad.DATATYPE.double,
            np.dtype(np.float128): ad.DATATYPE.long_double,
            np.dtype(np.complex64): ad.DATATYPE.complex,
            np.dtype(np.complex128): ad.DATATYPE.double_complex,
        }

    def read(self, msg):
        doid = msg['doid']
        column = msg['column']
        rows = msg['rows']
        rowid = msg['row']
        filename = self.filepath + '/' + doid
        f = ad.file(filename)
        msg['data'] = f.var[column][rowid:rowid+rows,:]

    def write(self, msg):

        doid = msg['doid']
        column = msg['column']
        rows = msg['rows']
        shape = msg['shape']
        rowid = msg['row']
        datatype = msg['datatype']
        data = msg['data']
        filename = self.filepath + '/' + doid

        dimension = [rows] + copy.copy(shape)
        global_dimension = copy.copy(dimension)
        global_dimension[0] = self.maxrows
        offset = [0] * len(dimension)
        offset[0] = rowid

        ad.init_noxml()
        ad.allocate_buffer (ad.BUFFER_ALLOC_WHEN.NOW, self.buffersize);
        adios_group = ad.declare_group("shore", "", ad.FLAG.YES)
        local_dimension = str(dimension)[1:-1]
        global_dimension = str(global_dimension)[1:-1]
        offset = str(offset)[1:-1]

        ad.select_method(adios_group, "POSIX", "", "")
        ad.define_var(adios_group, column, "", self.dtype_numpy2adios[datatype], local_dimension, global_dimension, offset)
        adios_file = ad.open("shore", filename, 'u')
        group_size = 1000000
        if data.nbytes > group_size:
            group_size = data.nbytes
        ad.set_group_size(adios_file, group_size)
        ad.write(adios_file, column, data, datatype)
        ad.close(adios_file)
        ad.finalize()

        return True




def get_class():
    return files_adios

