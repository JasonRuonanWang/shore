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
import os
from files import files

class files_hdf5(files):

    def __init__(self, event, config):
        files.__init__(self, event, config)
        self.min_rows = 100


    def delete(self, msg):
        filename = self.filepath + '/' + msg['doid']
        try:
            os.remove(filename)
        except:
            return False
        return True


    def read(self, msg):
        filename = self.filepath + '/' + msg['doid']
        datasetName = msg['column']
        rowid = msg['row']
        rows = msg['rows']
        if rows == 0:
            rows = msg['return']['do']['total_rows'] - rowid
        f = None
        try:
            f = h5py.File(filename)
        except Exception as e:
            print e
            return True
        if not f:
            self.log('backend.file.hdf5.read(): invalid file name {0}'.format(filename), category='error')
        if datasetName in f:
            msg['data'] = f[datasetName][rowid:rowid+rows,:]
        else:
            self.log('backend.file.hdf5.read(): invalid column name {0}'.format(datasetName), category='error')
        return True

    def write(self, msg):
        filename = self.filepath + '/' + msg['doid']
        datasetName = msg['column']
        shape = [self.min_rows] + msg['shape']
        maxshape = [None] + msg['shape']
        rowid = msg['row']
        rows = msg['rows']
        if rows <= 0:
            self.log('User trying to write a non-positive number of rows to hdf5.', category='warning', source=__name__)
            return True
        if rowid < 0:
            self.log('User trying to write data to a negative row number of an hdf5 file.', category='warning', source=__name__)
            return True

        f = None
        try:
            f = h5py.File(filename)
        except Exception as e:
            print e
            return True

        if not f:
            self.log('backend.file.hdf5.read(): invalid file name {0}'.format(filename), category='error')
        if datasetName in f:
            if f[datasetName].dtype != msg['datatype']:
                msg['return']['write'] = 'hdf5: datatype does not match'
                self.log('Data Object {0} Column {1} datatype does not match. Did not wirte anything.'.format(msg['doid'],msg['column']), category='warning', source=__name__)
                return True
            if list(f[datasetName].shape[1:]) != msg['shape']:
                msg['return']['write'] = 'hdf5: shape does not match'
                self.log('Data Object {0} Column {1} shape does not match. Did not wirte anything.'.format(msg['doid'],msg['column']), category='warning', source=__name__)
                return True
        else:
            f.create_dataset(datasetName, shape, msg['datatype'], maxshape=maxshape)

        if msg['row'] >= f[datasetName].shape[0]:
            nr_rows = (int(msg['row'] / self.min_rows) + 1) * self.min_rows
            f[datasetName].resize([nr_rows] + msg['shape'])

        f[datasetName][rowid:rowid+rows,:] = msg['data']
        return True

def get_class():
    return files_hdf5

