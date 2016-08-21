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
import cPickle as pickle
from shoreMeta.plugin import plugin


class shoreClient(plugin):

    message_socket = None
    transport_socket = None
    isInited = False

    def __init__(self, event = None, config = None):
        if event and config:
            plugin.__init__(self,event,config)


    def securityCheck(self, doid, column, row, rows):
        if type(row) is not int:
            print('ShoreClient Error: Please give a valid start row number')
            return False
        if type(rows) is not int:
            print('ShoreClient Error: Please give a valid total row number')
            return False
        return True

    def networkInit(self, address = None):
        import zmq
        if address:
            message_address = address
        else:
            message_address = os.environ.get('SHORE_DAEMON_ADDRESS', 'tcp://127.0.0.1:12306')
        transport_address = message_address.split(':')[0] + ':' + message_address.split(':')[1] + ':' + str(int(message_address.split(':')[2]) + 1)
        context = zmq.Context()
        self.message_socket = context.socket(zmq.REQ)
        self.message_socket.connect(message_address)
        self.transport_socket = context.socket(zmq.REQ)
        self.transport_socket.connect(transport_address)
        self.isInited = True

    def delete(self, doid, column=None):
        if not self.isInited:
            self.networkInit()
        msg_send = {
            'operation' : 'delete',
            'doid' : doid,
            'column' : column,
        }
        self.message_socket.send(pickle.dumps(msg_send))
        ret = pickle.loads(self.message_socket.recv())
        return ret

    def query(self, doid, column=None):
        if not self.isInited:
            self.networkInit()
        msg_send = {
            'operation' : 'query',
            'doid' : doid,
            'column' : column,
        }
        self.message_socket.send(pickle.dumps(msg_send))
        ret = pickle.loads(self.message_socket.recv())
        if type(ret) is not dict:
            return None
        if 'return' not in ret:
            return None
        if 'do' not in ret['return']:
            print('shoreClient.shoreGet(): Could not find Data Object {0}'.format(doid))
            return None
        if 'columns' not in ret['return']['do']:
            if column is None:
                return ret
            print('shoreClient.shoreGet(): Could not find Column {1} in Data Object {0}'.format(doid, column))
            return None
        if column not in ret['return']['do']['columns']:
            print('shoreClient.shoreGet(): Could not find Column {1} in Data Object {0}'.format(doid, column))
            return None
        return ret

    def get(self, doid, column = 'data', row = 0, rows = 1, slicer = None):
        if not self.securityCheck(doid,column,row,rows):
            return None

        if not self.isInited:
            self.networkInit()
        msg_send = {
            'operation' : 'get',
            'doid' : doid,
            'column' : column,
            'row' : row,
            'rows' : rows
        }
        self.message_socket.send(pickle.dumps(msg_send))
        ret = pickle.loads(self.message_socket.recv())
        if type(ret) is not dict:
            return None
        if 'return' not in ret:
            return None
        if 'do' not in ret['return']:
            print('shoreClient.shoreGet(): Could not find Data Object {0}'.format(doid))
            return None
        if 'columns' not in ret['return']['do']:
            print('shoreClient.shoreGet(): Could not find any columns in Data Object {0}'.format(doid))
            return None
        if column not in ret['return']['do']['columns']:
            print('shoreClient.shoreGet(): Could not find Column {1} in Data Object {0}'.format(doid, column))
            return None

        # transport
        if 'event_id' in ret:
            pkg_dict = {'event_id':ret['event_id'],'operation':'get'}
            pkg_pickled = pickle.dumps(pkg_dict)
            self.transport_socket.send(pkg_pickled)
            ret = self.transport_socket.recv()
            ret = pickle.loads(ret)
            if 'data' in ret:
                return ret['data']
            else:
                return None

    def put(self, data, doid, column = 'data', row = 0, rows = 1, slicer = None, backend = None):

        if not self.securityCheck(doid,column,row,rows):
            return None

        if not self.isInited:
            self.networkInit()
            print self.message_socket
            print 'client: networkInit()'
            print self.message_socket

        shape = list(data.shape)[1:]
        dtype = data.dtype
        # message
        msg_send = {
            'operation' : 'put',
            'doid' : doid,
            'column' : column,
            'row' : row,
            'rows': rows,
            'shape' : shape,
            'datatype' : dtype,
        }
        if slicer:
            msg_send['slicer']=slicer
        if backend:
            msg_send['backend']=backend
        self.message_socket.send(pickle.dumps(msg_send))
        ret = pickle.loads(self.message_socket.recv())

        # transport
        if 'event_id' in ret:
            msg_send = {'event_id':ret['event_id'], 'data':data, 'operation':'put'}
            self.transport_socket.send(pickle.dumps(msg_send))
            ret = self.transport_socket.recv()
            ret = pickle.loads(ret)

        return ret

def instance(event = None, config = None):
    return shoreClient(event, config)


