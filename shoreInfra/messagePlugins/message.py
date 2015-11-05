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

class message(plugin):

    def __init__(self, event):
        plugin.__init__(self,event)
        msg = {'operation':'admin', 'module':'message', 'config':'message_address'}
        self.push_event(msg)

    def event_handler_module(self, msg):
        # if admin event
        if self.msg_kv_match(msg, 'operation', 'admin'):
            if self.msg_kv_match(msg, 'command', 'init'):
                if msg.has_key['message_address']:
                    self.__url_clients = msg['message_address']
                    self.bind()
                    self.start()
                else:
                    self.log('tyring to start message module without a valid address', category='error', source=__name__)
            if self.msg_kv_match(msg, 'command', 'terminate'):
                self.stop()
            # don't push the message back into the event queue
            return False

        self.respond(msg)
        return True

    def start(self):
        for i in range(2):
            thread = threading.Thread(target=self.worker_routine, args=())
            self.__threads.append(thread)
            thread.start()
        self.start_plugin()

    def start_plugin(self):
        return

    def stop(self):
        t = threading.Thread(target=self.stop_thread)
        t.start()
        self.__looping = False


