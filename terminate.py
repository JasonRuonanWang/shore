#!/usr/local/bin/python

import zmq
import os
import uuid
import cPickle as pickle

address = os.environ.get('SHORE_DAEMON_ADDRESS', 'tcp://127.0.0.1:12306')

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(address)

socket.send(pickle.dumps({'command':'terminate','operation':'admin'}))
msg = pickle.loads(socket.recv())
print msg


