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

import copy

class plugin(object):

    def __init__(self, event):
        event.register_observer(self.event_handler)
        self.push_event = event.push_event
        self.log('{0} instantiated and registered to event channel.'.format(self.__class__.__name__), category='system')

    def event_handler(self, msg_recv):
        msg = copy.copy(msg_recv)

        # check if this module should respond
        if not self.msg_kv_match(msg, 'module', self.__class__.__name__.split('_')[0]):
            return False

        # check if the event's status is pre processing
        if not self.msg_kv_match(msg, 'status', 'pre'):
            return False

        # event_handler_module must return True to send msg back to workflow
        if self.event_handler_module(msg):
            msg['status'] = 'post'
            self.push_event(msg)

    def msg_kv_match(self, msg, k, v):
        if not msg.has_key(k):
            return False
        if msg[k] != v:
            return False
        return True

    def log(self, text, category=None, source=None, color=None, style=None):
        msg = { 'module':'log',
                'status':'pre',
                'color':color,
                'style':style,
                'text':text,
                'source':source,
                'category':category}
        self.push_event(msg)

    def plugin_name(self):
        return self.__class__.__name__.split('_')[1]

    def module_name(self):
        return self.__class__.__name__.split('_')[0]



