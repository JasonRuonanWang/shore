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
sys.path.append('shoreBackend/ramPlugins')
from ram import ram
import numpy as np


class ram_numpy(ram):

    def __init__(self, event, config):
        ram.__init__(self, event, config)
        self.__inmem = {}

    def read(self, msg):
        doid = msg['doid']
        column = msg['column']
        rowid = msg['row']
        rows = msg['rows']

        if doid in self.__inmem:
            if column in self.__inmem[doid]:
                msg['data'] = self.__inmem[doid][column]['data'][rowid:rowid+rows,:]


    def write(self, msg):

        doid = msg['doid']
        column = msg['column']
        rowid = msg['row']
        rows = msg['rows']
        data = msg['data']
        shape = msg['shape']
        datatype = msg['datatype']

        if doid not in self.__inmem:
            self.__inmem[doid] = {}
        if column not in self.__inmem[doid]:
            self.__inmem[doid][column] = {}
        if 'data' not in self.__inmem[doid][column]:
            self.__inmem[doid][column]['data'] = np.ndarray([rowid + rows] + shape, datatype)
        if rowid + rows > self.__inmem[doid][column]['data'].shape[0]:
            datatmp = np.ndarray([rowid + rows] + shape, datatype)
            datatmp[0:self.__inmem[doid][column]['data'].shape[0],:] = self.__inmem[doid][column]['data']
            self.__inmem[doid][column]['data'] = datatmp

        self.__inmem[doid][column]['data'][rowid:rowid+rows,:] = data

        return True


def get_class():
    return ram_numpy

