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

class retouch(plugin):

    def event_handler_admin(self, msg):
        return

    def event_handler_workflow(self, msg):
        # fix rows number if rows == 0
        if 'rows' in msg:
            if msg['rows'] == 0:
                if 'return' in msg:
                    if 'do' in msg['return']:
                        if 'total_rows' in msg['return']['do']:
                            if 'row' in msg:
                                msg['rows'] = msg['return']['do']['total_rows'] - msg['row']


        if 'backend' not in msg:
            msg['backend'] = self.config('backend_default')


        return True




