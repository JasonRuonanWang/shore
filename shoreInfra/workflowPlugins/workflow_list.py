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
from workflow import workflow

class workflow_list(workflow):

    flowlist_get = ['request', 'eventid', 'dodb', 'storage']
    flowlist_put = ['request', 'eventid', 'dodb', 'storage']
    flowlist_query = ['request', 'eventid', 'dodb']

    def event_handler_plugin(self, msg):
        next_module = self.get_next(self.flowlist_put, msg['module'])
        if next_module:
            msg['module'] = next_module
            msg['status'] = 'pre'
            self.push_event(msg)

    def get_next(self, flowlist, current):
        index = flowlist.index(current)
        if index + 1 == len(flowlist):
            return None
        else:
            return flowlist[index + 1]

    def get_previous(self, flowlist, current):
        index = flowlist.index(current)
        if index == 0:
            return None
        else:
            return flowlist[index - 1]


def get_class():
    return workflow_list


