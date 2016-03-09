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

    dtype_shore_to_raw={
        0:'bool',
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
        11:'string',
    }

    dtype_shore_to_numpy={
        0:numpy.bool,
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
        11:None,
    }

    def query(self,msg):
        dic = {'doid':msg['doid']}
        do_list = self.db_query('do', dic)
        if len(do_list) > 0:
            msg['return']['do'] = do_list[0]
            if len(do_list) > 1:
                self.log('doid {0} found multiple records'.format(msg['doid']), category='error', source=__name__)

        if 'column' in msg:
            dic = {'doid':msg['doid'], 'column':msg['column']}
            column_list = self.db_query('column', dic)
            if len(column_list) > 0:
                msg['return']['column'] = column_list[0]
                if len(column_list) > 1:
                    self.log('doid {0}, column {1} found multiple records'.format(msg['doid'],msg['column']), category='error', source=__name__)

    def update(self,msg):
        query_dict = {'doid':msg['doid']}
        do_list = self.db_query('do', query_dict)
        if len(do_list) > 0:
            self.db_update('do', query_dict, {'rows':msg['row']}, 'max')
            self.db_update('do', query_dict, {'columns':msg['column']}, 'add')
        else:
            self.db_insert('do', {'doid':msg['doid'], 'rows':msg['row'], 'columns':[msg['column']]})

        query_dict = {'doid':msg['doid'], 'column':msg['column']}
        column_list = self.db_query('column', query_dict)
        msg['datatype_numpy'] = self.dtype_shore_to_numpy[msg['datatype']].__name__
        if len(column_list) > 0:
            if column_list[0]['shape'] !=msg['shape']:
                msg['return']['dodb'] = 'Shape not match'
                self.log('Data Object {0} Column {1} shape does not match'.format(msg['doid'],msg['column']), category='warning', source=__name__)
        else:
            self.db_insert('column', {'doid':msg['doid'], 'column':msg['column'], 'shape':msg['shape'], 'datatype':msg['datatype'], 'datatype_numpy':msg['datatype_numpy']})


    def event_handler_admin(self, msg):
        return

    def event_handler_workflow(self, msg):
        if not 'doid' in msg:
            self.log('query dodb without having valid data object ID', category='error', source=__name__)
            return False

        operation = msg.get('operation')
        if operation == 'put':
            self.update(msg)
        elif operation == 'get' or 'query':
            self.query(msg)
        else:
            self.log('dodb.event_handler_workflow received invalid msg[\'operation\']', category='warning', source=__name__)
            return False
        return True



