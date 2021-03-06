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

from workflow import workflow

class workflow_list(workflow):

    __flowlist={}
    __flowlist['put'] = {}
    __flowlist['put']['message'] = ['authen', 'retouch', 'eventid', 'dodb', 'queue', 'message']
    __flowlist['put']['transport'] = ['queue', 'retouch', 'storage', 'profiling', 'transport']
    __flowlist['put']['transport_nonblocking'] = ['queue', 'retouch', 'transport', 'storage', 'profiling']
    __flowlist['get'] = {}
    __flowlist['get']['message'] = ['authen', 'retouch', 'eventid', 'dodb', 'queue', 'message']
    __flowlist['get']['transport'] = ['queue', 'retouch', 'storage', 'profiling', 'transport']
    __flowlist['get']['transport_nonblocking'] = __flowlist['get']['transport']
    __flowlist['query'] = {}
    __flowlist['query']['message'] = ['authen', 'eventid', 'dodb', 'message']
    __flowlist['delete'] = {}
    __flowlist['delete']['message'] = ['authen', 'eventid', 'dodb', 'message', 'storage']

    def get_next(self, operation, workflow, current):
        index = self.__flowlist[operation][workflow].index(current)
        if index + 1 == len(self.__flowlist[operation][workflow]):
            return None
        else:
            return self.__flowlist[operation][workflow][index + 1]

    def get_first(self, operation, workflow):
        return self.__flowlist[operation][workflow][0]

def get_class():
    return workflow_list


