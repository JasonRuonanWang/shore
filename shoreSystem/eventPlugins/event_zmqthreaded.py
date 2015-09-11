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
import threading
import time
import json
import os
from event import event

class event_zmqthreaded(event):

    __context = zmq.Context.instance()
    __isbound = False
    __socket_clients = None
    __socket_workers = None
    __socket_worker = None
    __url_workers = "inproc://workers"
    __threads = []

    def __init__(self, address):
        self.__url_clients = address
        self.bind()

    def worker_routine(self):
        self.__socket_worker = self.__context.socket(zmq.REP)
        self.__socket_worker.connect(self.__url_workers)
        msg = None
        while True:
            msg = self.__socket_worker.recv_json()
            if isinstance(msg, dict):
                self.__socket_worker.send_json({"return": "OK"})
                if msg.has_key('operation'):
                    if msg['operation'] == 'exit':
                        self.__socket_worker.close()
                        t = threading.Thread(target=self.stop)
                        t.start()
                        break
                self.notify_observers(msg)
            else:
                self.__socket_worker.send_json({"return": "Error: Wrong JSON Object"})
                continue
#        output.printf("system.event.zmqthreaded: Worker thread is terminated!", 'blue')

    def bind(self):
        while True:
            self.__socket_clients = self.__context.socket(zmq.ROUTER)
            self.__socket_workers = self.__context.socket(zmq.DEALER)
            try:
                self.__socket_clients.bind(self.__url_clients)
                self.__socket_workers.bind(self.__url_workers)
                self.__isbound = True
#                output.printf('bound {0}'.format(self.__url_clients),'blue')
                return
            except:
#                output.exception(__name__,'unable to bind address {0}'.format(self.__url_clients),'')
                self.__url_clients = raw_input('please re-enter the local address:')

    def start(self):
        for i in range(1):
            thread = threading.Thread(target=self.worker_routine, args=())
            self.__threads.append(thread)
            thread.start()
        try:
            zmq.device(zmq.QUEUE, self.__socket_clients, self.__socket_workers)
        except:
#            output.printf("ZMQ Device is terminated!", 'blue')
            return

    def stop(self):
        self.__socket_workers.close()
        self.__socket_clients.close()
        time.sleep(1)
        self.__context.term()
#        output.printf("ZMQ Context is terminated!", 'blue')





def get_class():
    return event_zmqthreaded


