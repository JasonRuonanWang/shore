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

import mpi4py
import time
from message import message
import cPickle as pickle

class message_mpi(message):

    _looping = False

    def respond(self, msg):
        pass

    def start_thread(self):
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
        self.log("Worker thread is terminated!", category='system')

    def start_plugin(self):
        while self._looping:
            sleep(1)

    def stop_thread(self):
        pass

def get_class():
    return message_mpi

