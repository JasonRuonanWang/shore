#!/usr/bin/python

import zmq
import os

address = os.environ['SHORE_DAEMON_ADDRESS']

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(address)

socket.send_json({'command':'terminate'})
r = socket.recv_json()
print r


