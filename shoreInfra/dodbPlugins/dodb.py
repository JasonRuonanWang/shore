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
#	 Any bugs, problems, and/or suggestions please email to
#	 jason.wang@icrar.org or jason.ruonan.wang@gmail.com

import sys
sys.path.append('shoreMeta')
from plugin import plugin

class dodb(plugin):

    def put(self, doid, column, row, shape=None):
        self.update_do(doid, column, int(row)+1)
        self.update_column(doid, column, shape)

    def get(self, doid, column, row):
        return

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
            self.put(msg['doid'], msg['column'], msg['row'], msg['shape'])
        elif msg['operation'] == 'get':
            self.get(msg['doid'], msg['column'], msg['row'])

        return True



