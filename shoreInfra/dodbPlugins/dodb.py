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

    def put(self, doid, column, row):
        print self.query_do(doid)
        return

    def get(self, doid, column, row):
        return

    def event_handler_module(self, msg):
        if not msg.has_key('doid'):
            self.printf('Error: query dodb without having valid data object ID', color='red', source=__name__)
            return False
        if not msg.has_key('operation'):
            self.printf('Error: msg does not specify operation to do', color='red', source=__name__)
            return False

        if msg['operation'] == 'put':
            self.put(msg['doid'], msg['column'], msg['row'])

        return True



