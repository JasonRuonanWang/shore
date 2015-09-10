#!/usr/bin/python

import zmq
import json
import os

address = os.environ['SHORE_DAEMON_ADDRESS']

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(address)

socket.send_json({'operation':'exit'})
r = socket.recv_json()
print r


