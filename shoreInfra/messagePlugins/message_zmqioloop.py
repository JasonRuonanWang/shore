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
from zmq.eventloop.zmqstream import ZMQStream
from zmq.eventloop.ioloop import IOLoop
import time
import threading
from message import message


class message_zmqioloop(message):

    def __init__(self, address):
        self.__isbound = None
        self.__stream = None
        self.__url = address
        self.__socket = None
        self.__bind()

    def __del__(self):
        if self.__isbound:
            self.__unbind()

    def bind(self):
        while True:
            try:
                self.context = zmq.Context(10)
                self.__socket = self.context.socket(zmq.REP)
                self.__socket.bind(self.__url)
                self.__isbound = True
#                output.printf('bound {0}'.format(self.__url),'blue')
                self.__stream = ZMQStream(self.__socket)
                return
            except:
#                output.exception(__name__,'unable to bind address'.format(self.__url),'')
                self.__url = raw_input('please re-enter the local address:')

    def unbind(self):
        try:
            self.__socket.unbind(self.__url)
            self.__isbound = False
#            output.printf('unbound {0}'.format(self.__url),'blue')
        except:
#            output.exception(__name__,'unable to unbind address'.format(self.__url),'')
            pass

    def start(self):
        def on_recv(stream, msg):
            self._mainloop(msg)
            stream.send('OK')
            if msg[0] == "exit":
                t = threading.Thread(target=self.__stop)
                t.start()
        self.__stream.on_recv_stream(on_recv)
        IOLoop.instance().start()

    def stop(self):
        time.sleep(1)
        IOLoop.instance().stop()



def get_class():
    return message_zmqioloop


