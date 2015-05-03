#!/usr/bin/python

import domashSystem as system
import zmq
import json

config = system.config.default()
address = config.value('address')

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(address)

socket.send_json({'operation':'exit'})
r = socket.recv_json()
print r


