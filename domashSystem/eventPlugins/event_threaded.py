#
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

import zmq
import sys
sys.path.append('../domashMeta')
import output
import threading
from event import event

class event_threaded(event):

    __isbound = False
    __socket_clients = None
    __socket_workers = None
    __socket_worker = None
    __url_workers = "inproc://workers"

    def __init__(self, address):
        self.__url_clients = address
        self.__bind()

    def __worker_routine(self, context=None):
        context = context or zmq.Context.instance()
        self.__socket_worker = context.socket(zmq.REP)
        self.__socket_worker.connect(self.__url_workers)
        while True:
            msg = self.__socket_worker.recv()
            self._mainloop(msg)
            self.__socket_worker.send("OK")
            if msg == "exit":
                sys.exit()


    def __del__(self):
        if self.__isbound:
            self.__unbind()

    def __bind(self):
        while True:
            context = zmq.Context.instance()
            self.__clients = context.socket(zmq.ROUTER)
            self.__workers = context.socket(zmq.DEALER)
            try:
                self.__clients.bind(self.__url_clients)
                self.__workers.bind(self.__url_workers)
                self.__isbound = True
                output.printf('bound {0}'.format(self.__url_clients),'blue')
                return
            except:
                output.exception(__name__,'unable to bind address {0}'.format(self.__url_clients),'')
                self.__url_clients = raw_input('please re-enter the local address:')

    def __unbind(self):
        try:
            self.socket.unbind(self.__url_clients)
            self.__isbound = False
            output.printf('unbound {0}'.format(self.__url_clients),'blue')
        except:
            output.exception(__name__,'unable to unbind address'.format(self.__url_clients),'')

    def start(self):
        for i in range(1):
            thread = threading.Thread(target=self.__worker_routine, args=())
            thread.start()
        zmq.device(zmq.QUEUE, self.__clients, self.__workers)

def get_class():
    return event_threaded


