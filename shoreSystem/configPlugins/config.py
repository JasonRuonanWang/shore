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


import os
import copy
from shoreMeta.plugin import plugin

class config(plugin):

    def __init__(self, event):
        plugin.__init__(self,event,self)
        message_address = os.environ.get('SHORE_DAEMON_ADDRESS', 'tcp://0.0.0.0:12306')
        shore_root = os.environ.get('SHORE_ROOT', '/scratch/shore')
        db_address = os.environ.get('SHORE_MONGO_ADDRESS', 'mongodb://localhost:27017')
        print db_address
        transport_address = message_address.split(':')[0] + ':' + message_address.split(':')[1] + ':' + str(int(message_address.split(':')[2]) + 1)
        self.__config_dict__ = {
            # system
            'log':'standard',
            'event':'observer',
            'workflow':'list',
            # infrastructure
            'authen':'null',
            'dodb':'mongo',
            'db_address':db_address,
            'eventid':'uuid',
            'message':'zmqthreaded',
            'message_address':message_address,
            'transport':'zmqthreaded',
            'transport_address':transport_address,
            'transport_workflow':'transport_nonblocking',
 #           'transport_workflow':'transport',
            'queue':'dict',
            'retouch':'default',
            'profiling':'mongo',
            # backend
            'backend_default':'mongo',
            'filesystems':[
                {'root':shore_root, 'type':'HFS+', 'device':'HDD'},
                {'root':'/scratch/ssd', 'type':'EXT3', 'device':'SSD'},
            ],
            'backend_adios':0,
            'backend_hdf5':0,
        }

    def value(self, key):
        if key in self.__config_dict__:
            return self.__config_dict__[key]
        else:
            print ('Error: Key {0} not found in config!'.format(key))

    def print_dict(self):
        print (self.__config_dict__)

    def event_handler(self, msg_recv):
        msg = copy.copy(msg_recv)
        if not 'config' in msg:
            return False
        if not msg['config'] in self.__config_dict__:
            return False
        if msg['config'] in msg:
            return False
        msg[msg['config']] = self.__config_dict__[msg['config']]
        self.push_event(msg, self.__class__.__name__)

