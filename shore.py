#!/usr/local/bin/python
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


def start_daemon():

    import shoreSystem as system
    import shoreInfra as infra
    import shoreBackend as backend

    event = system.event.observer()
    config = system.config.default(event)
    eval("system.log.{0}(event, config)".format(config.value('log')))
    eval("system.workflow.{0}(event, config)".format(config.value('workflow')))

    for module in infra.plugin_dict:
        for plugin in infra.plugin_dict[module]:
            if plugin == config.value(module):
                eval("infra.{0}.{1}(event, config)".format(module, plugin))

    for module in backend.plugin_dict:
        for plugin in backend.plugin_dict[module]:
            eval("backend.{0}.{1}(event, config)".format(module, plugin))

    event.push_event({'operation':'admin', 'command':'start'}, __name__)

def stop_daemon(address = None):

    import zmq
    import os
    import uuid
    import cPickle as pickle

    if not address:
        address = os.environ.get('SHORE_DAEMON_ADDRESS', 'tcp://127.0.0.1:12306')

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(address)

    socket.send(pickle.dumps({'command':'terminate','operation':'admin'}))
    msg = pickle.loads(socket.recv())
    print msg

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        start_daemon()
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'start':
            start_daemon()
        elif sys.argv[1] == 'stop':
            stop_daemon()





