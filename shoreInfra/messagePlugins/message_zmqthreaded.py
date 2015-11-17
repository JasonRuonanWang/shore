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

    _context = zmq.Context.instance()
    _socket_clients = None
    _socket_workers = None
    _url_workers = "inproc://message_workers"
    _looping = False

    def respond(self, msg):
        if msg.has_key('zmq_worker'):
            if msg.has_key('event_id'):
                msg['zmq_worker'].send_json({"event_id": str(msg['event_id'])})
            elif msg.has_key('command'):
                msg['zmq_worker'].send_json({msg['command']: 'OK'})
            else:
                msg['zmq_worker'].send_json({'Unknown': 'OK'})
        else:
            self.log('No zmq_worker handler in msg',category='error')
        pass

    def bind(self):
        while True:
            self._socket_clients = self._context.socket(zmq.ROUTER)
            self._socket_workers = self._context.socket(zmq.DEALER)
            try:
                self._socket_clients.bind(self._url_clients)
                self._socket_workers.bind(self._url_workers)
                self.log('bound {0}'.format(self._url_clients), category='system')
                return
            except:
                self.log('unable to bind address {0}'.format(self._url_clients), category='error')
                pass

    def start_thread(self):
        _socket_worker = self._context.socket(zmq.REP)
        _socket_worker.connect(self._url_workers)
        msg = None
        while self._looping:
            try:
                msg = _socket_worker.recv_json()
                if isinstance(msg, dict):
                    msg['zmq_worker'] = _socket_worker # send worker with msg so that it can be used for sending reply when pushed back to event module
                    self.push_event(msg, self.__class__.__name__)
            except:
                self._looping = False
                self.log("Worker recv_json() is broken!", category='system')
        _socket_worker.close()
        self.log("Worker thread is terminated!", category='system')

    def start_plugin(self):
        try:
            zmq.device(zmq.QUEUE, self._socket_clients, self._socket_workers)
        except:
            self.log("ZMQ Device is terminated!", category='system')

    def stop_thread(self):
        time.sleep(1)
        self._socket_workers.close()
        self._socket_clients.close()
        self._context.term()
        self.log("ZMQ Context is terminated!", category='system')

def get_class():
    return message_zmqthreaded
