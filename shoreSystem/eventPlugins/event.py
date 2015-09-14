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

class event(plugin):

    __observers = []

    # Plugins should register this method for later pushing events to the notifier
    # It is also called within system.event.<subclass> on receiving a request from sockets
    def push_event(self, msg):
        for observer in self.__observers:
            observer(msg)

    def print_observers(self):
        for observer in self.__observers:
            print observer

    # Every plugin should call this method to register its event handler method
    def register_observer(self, func):
        self.__observers.append(func)

    # overwrite event_handler because event plugins have different behaviours than general plugins
    def event_handler(self, msg):
        if not self.msg_kv_match(msg, 'module', self.__class__.__name__.split('_')[0]):
            return False
        if self.msg_kv_match(msg, 'command', 'terminate'):
            self.stop()





