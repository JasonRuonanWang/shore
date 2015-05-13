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
sys.path.append('domashMeta')
import output
sys.path.append('domashInfra')
from infra import infra

class storage(infra):

    def event_handler_module(self, msg):


        # verify if this plugin should respond
        if not msg.has_key('backend'):
            return False
        if msg['backend'] != self.__class__.__name__.split('_')[-1]:
            return False

        if not msg.has_key('operation'):
            return False
        return True


    def read(self):
        output.printf('infra.storage.read() is a pure virtual function and you must implement it in a derived class','red')

    def write(self):
        output.printf('infra.storage.write() is a pure virtual function and you must implement it in a derived class','red')





