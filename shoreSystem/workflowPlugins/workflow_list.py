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


from workflow import workflow

class workflow_list(workflow):

    __flowlist={}
    __flowlist['get'] = ['authen', 'eventid', 'dodb', 'storage']
    __flowlist['put'] = ['authen', 'eventid', 'message', 'dodb', 'storage']
    __flowlist['query'] = ['authen', 'eventid', 'dodb']

    def event_handler_plugin(self, msg):
        next_module = self.get_next(msg['operation'], msg['module'])
        if next_module:
            msg['module'] = next_module
            msg['status'] = 'pre'
            return True
        return False

    def get_next(self, operation, current):
        index = self.__flowlist[operation].index(current)
        if index + 1 == len(self.__flowlist[operation]):
            return None
        else:
            return self.__flowlist[operation][index + 1]

    def get_previous(self, flowlist, current):
        index = flowlist.index(current)
        if index == 0:
            return None
        else:
            return flowlist[index - 1]

    def get_first(self, operation):
        return self.__flowlist[operation][0]


def get_class():
    return workflow_list


