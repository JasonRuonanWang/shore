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

import zmq
import time
from message import message

class message_zmqthreaded(message):

    __context = zmq.Context.instance()
    __isbound = False
    __socket_clients = None
    __socket_workers = None
    __url_workers = "inproc://message_workers"
    __threads = []
    __looping = True


    def respond(self, msg):
        if msg.has_key('zmq_worker'):
            msg['zmq_worker'].send_json({"event_id": str(msg['event_id'])})
        else:
            self.log('No zmq_worker handler in msg',category='error', source=__name__)

    def bind(self):
        while True:
            self.__socket_clients = self.__context.socket(zmq.ROUTER)
            self.__socket_workers = self.__context.socket(zmq.DEALER)
            try:
                self.__socket_clients.bind(self.__url_clients)
                self.__socket_workers.bind(self.__url_workers)
                self.__isbound = True
                self.log('bound {0}'.format(self.__url_clients),category='system')
                return
            except:
                self.log('unable to bind address {0}'.format(self.__url_clients),source=__name__,category='error')
                self.__url_clients = raw_input('please re-enter the local address:')

    def start_thread(self):
        __socket_worker = self.__context.socket(zmq.REP)
        __socket_worker.connect(self.__url_workers)
        msg = None
        while self.__looping:
            try:
                msg = __socket_worker.recv_json()
            except:
                self.log("system.event.zmqthreaded: Worker recv_json() is broken!",category='system')
            if isinstance(msg, dict):
                msg['zmq_worker'] = __socket_worker # send worker with msg so that it can be used for sending reply when pushed back to event module
                self.push_event(msg)
        __socket_worker.close()
        self.log("system.event.zmqthreaded: Worker thread is terminated!",category='system')

    def start_plugin(self):
        try:
            zmq.device(zmq.QUEUE, self.__socket_clients, self.__socket_workers)
        except:
            self.log("ZMQ Device is terminated!", category='system')

    def stop_thread(self):
        self.__socket_workers.close()
        time.sleep(1)
        self.__socket_clients.close()
        self.__context.term()
        self.log("ZMQ Context is terminated!", category='system')

def get_class():
    return message_zmqthreaded

