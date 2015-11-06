#!/usr/bin/python

import zmq
import os
import uuid

address = os.environ['SHORE_DAEMON_ADDRESS']

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(address)

socket.send_json({'command':'terminate','operation':'admin'})
msg = socket.recv_json()
#msg['event_id'] = uuid.UUID(msg['event_id']).hex
print msg


