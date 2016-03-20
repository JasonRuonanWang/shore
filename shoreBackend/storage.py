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

from shoreMeta.plugin import plugin
from datetime import datetime

class storage(plugin):

    backend_list = []
    filesystem = None

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
        self.backend_list.append(self.plugin_name())

    def event_handler_workflow(self, msg):
        if not self.msg_kv_match(msg, 'backend', self.plugin_name()):
            return False


        operation = msg.get('operation')
        before = datetime.now()
        if operation == 'put':
            if self.write(msg):
                msg['return']['storage'] = 'OK'
            else:
                msg['return']['storage'] = 'ERROR'
        elif operation == 'get':
            if msg['row'] + msg['rows'] > msg['return']['do']['total_rows']:
                self.log('backend.storage.event_handler_workflow(): user trying to read more rows than existing', category='warning')
                return True
            if self.read(msg):
                msg['return']['storage'] = 'OK'
            else:
                msg['return']['storage'] = 'ERROR'
        elif operation == 'delete':
            if self.delete(msg):
                msg['return']['storage'] = 'OK'
            else:
                msg['return']['storage'] = 'ERROR'
        after = datetime.now()

        if msg['return']['storage'] == 'OK':
            msg['total_seconds'] = (after - before).total_seconds()
        if self.filesystem:
            msg['filesystem'] = self.filesystem
        return True







