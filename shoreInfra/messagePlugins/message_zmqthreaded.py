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
import cPickle as pickle

class message_zmqthreaded(message):

    _context = zmq.Context.instance()
    _socket_clients = None
    _socket_workers = None
    _url_workers = "inproc://message_workers"
    _looping = False

    def respond(self, msg):
        try:
            if 'zmq_worker' in msg:
                msg_send={}
                if 'event_id' in msg:
                    msg_send['event_id'] = msg['event_id']
                if 'return' in msg:
                    msg_send['return'] = msg['return']
                if 'command' in msg:
                    msg_send[msg['command']] = 'OK'
                msg['zmq_worker'].send(pickle.dumps(msg_send))
            else:
                self.log('No zmq_worker handler in msg',category='error')
            pass
        except Exception as e:
            import traceback, os.path
            top = traceback.extract_stack()[-1]
            print ', '.join([type(e).__name__, os.path.basename(top[0]), str(top[1])])

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
#            try:
                msg_recv = _socket_worker.recv()
                try:
                    msg = pickle.loads(msg_recv)
                except:
                    _socket_worker.send(pickle.dumps({'error': 'msg not unpickleable'}))
                    self.log('message_zmqthreaded received msg not unpickleable', category='error')
                if isinstance(msg, dict):
                    msg['workflow'] = 'message'
                    msg['return'] = {}
                    msg['zmq_worker'] = _socket_worker # send worker with msg so that it can be used for sending reply when pushed back to event module
                    self.push_event(msg, self.__class__.__name__)
#            except Exception as e:
#                self._looping = False
#                self.log("Worker recv_json() is broken!", category='system')
#                print e
#                import traceback, os.path
#                top = traceback.extract_stack()[-1]
#                print ', '.join([type(e).__name__, os.path.basename(top[0]), str(top[1])])
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
        time.sleep(1)
        self._context.term()
        self.log("ZMQ Context is terminated!", category='system')

def get_class():
    return message_zmqthreaded

