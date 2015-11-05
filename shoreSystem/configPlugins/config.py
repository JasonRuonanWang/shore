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

class config(plugin):

    def __init__(self):
        self.__config_dict__ = {
            # system
            'log':'standard',
            'event':'observer',
            'workflow':'list',
            # infrastructure
            'authen':'null',
            'dodb':'mongo',
            'eventid':'uuid',
            'message':'zmqthreaded',
            'transport':'zmqthreaded',
        }

    def value(self, key):
        if self.__config_dict__.has_key(key):
            return self.__config_dict__[key]
        else:
            print 'Error: Key {0} not found in config!'.format(key)

    def print_dict(self):
        print self.__config_dict__

    def event_handler(self, msg):
        if not msg.has_key('config'):
            return False







