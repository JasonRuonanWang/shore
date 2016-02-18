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

def shorePut(doid, column, row, shape, dtype, data):
    global message_socket
    msg = {
        'operation' : 'put',
        'doid' : doid,
        'column' : column,
        'row' : row,
        'shape' : shape,
        'datatype' : dtype,
    }
    message_socket.send_json(msg)
    ret = message_socket.recv_json()
    print ret

    if 'event_id' in ret:
        if shape:
            data_np = np.asarray(data)
            data_np_rs = data_np.reshape(shape)
            print data_np_rs
            pkg_dict = {'event_id':ret['event_id'], 'data':data_np_rs}
            pkg_pickled = pickle.dumps(pkg_dict)
            transport_socket.send(pkg_pickled)
            ret = transport_socket.recv_json()
            print ret
        else:
            pass

