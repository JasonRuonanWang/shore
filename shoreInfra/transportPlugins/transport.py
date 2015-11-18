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
import threading

class transport(plugin):

    _threads = []

    def event_handler_admin(self, msg):
        if self.msg_kv_match(msg, 'command', 'start'):
            if 'transport_address' in msg:
                self._url_clients = msg['transport_address']
                self.bind()
                self.start()
                return False
            else:
                if not 'config' in msg:
                    msg['config']='transport_address'
                    self.push_event(msg, self.__class__.__name__)
                return False
        if self.msg_kv_match(msg, 'command', 'terminate'):
            self.stop()
            return False
        return False

    def event_handler_workflow(self, msg):
        self.respond(msg)
        return True

    def start(self):
        self._looping = True
        for i in range(2):
            thread = threading.Thread(target=self.start_thread)
            self._threads.append(thread)
            thread.start()

        thread = threading.Thread(target=self.start_plugin)
        thread.start()

    def stop(self):
        self._looping = False
        t = threading.Thread(target=self.stop_thread)
        t.start()


