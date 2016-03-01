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

import h5py
from files import files

class files_hdf5(files):

    def __init__(self, event, config):
        files.__init__(self, event, config)
        self.min_rows = 100

    def read(self, msg):
        filename = self.filepath + '/' + msg['doid']
        f = h5py.File(filename)
        datasetName = msg['column']
        msg['data'] = f[datasetName][:]

    def write(self, msg):
        filename = self.filepath + '/' + msg['doid']
        f = h5py.File(filename)

        datasetName = msg['column']
        shape = [self.min_rows] + msg['shape']
        maxshape = [None] + msg['shape']
        if datasetName in f:
            if f[datasetName].dtype != msg['datatype']:
                msg['return'] = 'datatype does not match'
                return False
            if list(f[datasetName].shape[1:]) != msg['shape']:
                msg['return'] = 'shape does not match'
                return False
        else:
            f.create_dataset(datasetName, shape, msg['datatype'], maxshape=maxshape)

        if msg['row'] >= f[datasetName].shape[0]:
            nr_rows = (int(msg['row'] / self.min_rows) + 1) * self.min_rows
            f[datasetName].resize([nr_rows] + msg['shape'])

        f[datasetName][msg['row'],:] = msg['data']
        return True

def get_class():
    return files_hdf5




