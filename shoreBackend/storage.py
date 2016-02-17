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
sys.path.append('shoreMeta')
from plugin import plugin

class storage(plugin):

    dtype={0:'bool',
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

    def __init__(self, event, config):
        plugin.__init__(self, event, config)
        self.module_name = 'storage'

    def event_handler_workflow(self, msg):
        if not self.msg_kv_match(msg, 'backend', self.plugin_name()):
            return False

        operation = msg.get('operation', None)
        if operation == 'put':
            self.write(msg)
        elif operation == 'get':
            self.read(msg)
        return True







