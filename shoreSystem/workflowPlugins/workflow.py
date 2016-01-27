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
import copy

class workflow(plugin):

    # overwrite plugin.event_handler
    def event_handler(self, msg_recv):
        msg = copy.copy(msg_recv)
        if not 'operation' in msg:
            return False
        oper = msg['operation']
        if not 'workflow' in msg:
            return False
        work = msg['workflow']
        if oper == 'put' or oper == 'get' or oper == 'query':
            # in case there isn't 'module' key, add it and start from the beginning of the workflow
            if not 'module' in msg:
                msg['module'] = self.get_first(oper,work)
                msg['status'] = 'pre'
                self.push_event(msg, self.__class__.__name__)
                return
            # in case status is post, get to the next module
            if msg['status'] == 'post':
                next_module = self.get_next(msg['operation'], msg['workflow'], msg['module'])
                if next_module:
                    msg['module'] = next_module
                    msg['status'] = 'pre'
                    self.push_event(msg, self.__class__.__name__)




