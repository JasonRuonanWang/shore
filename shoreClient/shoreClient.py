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

import os
import zmq
import numpy as np
import cPickle as pickle

message_socket = None
transport_socket = None

def shoreZmqInit():
    global message_socket
    global transport_socket
    message_address = os.environ['SHORE_DAEMON_ADDRESS']
    transport_address = message_address.split(':')[0] + ':' + message_address.split(':')[1] + ':' + str(int(message_address.split(':')[2]) + 1)
    context = zmq.Context()
    message_socket = context.socket(zmq.REQ)
    message_socket.connect(message_address)
    transport_socket = context.socket(zmq.REQ)
    transport_socket.connect(transport_address)

def shoreQuery(doid, column, row):
    msg_send = {
        'operation' : 'query',
        'doid' : doid,
        'column' : column,
        'row' : row,
    }
    message_socket.send(pickle.dumps(msg_send))
    ret = pickle.loads(message_socket.recv())
    print ret


def shoreGet(doid, column, row):
    # message
    msg_send = {
        'operation' : 'get',
        'doid' : doid,
        'column' : column,
        'row' : row,
    }
    message_socket.send(pickle.dumps(msg_send))
    ret = pickle.loads(message_socket.recv())
    print ret
    # transport
    if 'event_id' in ret:
        pkg_dict = {'event_id':ret['event_id']}
        pkg_pickled = pickle.dumps(pkg_dict)
        transport_socket.send(pkg_pickled)
        ret = transport_socket.recv()
        ret = pickle.loads(ret)
        print ret
        if 'data' in ret:
            return ret['data']
        else:
            print ('Error: no data found')

def shorePut(doid, column, row, shape, dtype, data):
    # message
    msg_send = {
        'operation' : 'put',
        'doid' : doid,
        'column' : column,
        'row' : row,
        'shape' : shape,
        'datatype' : dtype,
    }
    message_socket.send(pickle.dumps(msg_send))
    ret = pickle.loads(message_socket.recv())

    # transport
    if 'event_id' in ret:
        if shape:
            data_np = np.asarray(data)
            data_np_rs = data_np.reshape(shape)
            print data_np_rs
            pkg_dict = {'event_id':ret['event_id'], 'data':data_np_rs}
            pkg_pickled = pickle.dumps(pkg_dict)
            transport_socket.send(pkg_pickled)
            ret = transport_socket.recv()
            ret = pickle.loads(ret)
            print ret
        else:
            pass

