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

class profiling(plugin):

    def event_handler_admin(self, msg):
        return

    def event_handler_workflow(self, msg):

        if 'total_seconds' in msg:
            dtype = msg['datatype']
            nBytes = msg['rows']
            for i in msg['shape']:
                nBytes *= i
            if dtype == 'int16':
                nBytes *= 2
            elif dtype == 'uint16':
                nBytes *= 2
            elif dtype == 'int32':
                nBytes *= 4
            elif dtype == 'uint32':
                nBytes *= 4
            elif dtype == 'float32':
                nBytes *= 4
            elif dtype == 'float64':
                nBytes *= 8
            elif dtype == 'complex64':
                nBytes *= 8
            elif dtype == 'complex128':
                nBytes *= 16

            nMBytes = float(nBytes) / 1000000
            MBps = "%.2f" % (nMBytes / msg['total_seconds'])
            dic = {'doid':msg['doid'],
                   'column':msg['column'],
                   'row':msg['row'],
                   'rows':msg['rows'],
                   'shape':msg['shape'],
                   'backend':msg['backend'],
                   'total_seconds':msg['total_seconds'],
                   'MBytes':nMBytes,
                   'MBps':MBps,
                   'datatype':str(dtype),
                   'operation':msg['operation']
                   }
            if 'filesystem' in msg:
                dic['filesystem'] = msg['filesystem']
            self.db_insert(dic)

        return True



