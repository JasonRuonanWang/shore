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
import numpy
sys.path.append('shoreMeta')
from plugin import plugin

class dodb(plugin):

    dtype_shore_to_raw={0:'bool',
           1:'char',
           2:'unsigned char',
           3:'short',
           4:'unsigned short',
           5:'int',
           6:'unsigned int',
           7:'float',
           8:'double',
           9:'complex',
           10:'double complex',
           11:'string'}

    dtype_shore_to_numpy={0:numpy.bool,
           1:numpy.int8,
           2:numpy.uint8,
           3:numpy.int16,
           4:numpy.uint16,
           5:numpy.int32,
           6:numpy.uint32,
           7:numpy.float32,
           8:numpy.float64,
           9:numpy.complex64,
           10:numpy.complex128,
           11:None}

    def query(self, msg):
        self.query_do(msg)
        self.query_column(msg)

    def update(self, msg):
        self.update_do(msg)
        self.update_column(msg)

    def get(self, msg):
        self.query_do(msg)
        self.query_column(msg)

    def event_handler_admin(self, msg):
        return

    def event_handler_workflow(self, msg):
        if not 'doid' in msg:
            self.log('query dodb without having valid data object ID', category='error', source=__name__)
            return False
        if not 'operation' in msg:
            self.log('msg does not specify operation to do', category='error', source=__name__)
            return False

        if msg['operation'] == 'put':
            if not 'shape' in msg:
                msg['shape'] = None
            if not 'column' in msg:
                msg['column'] = None
            if not 'row' in msg:
                msg['row'] = None
            self.update(msg)
        elif msg['operation'] == 'get':
            self.get(msg)
        elif msg['operation'] == 'query':
            self.query(msg)

        return True



