#!/usr/bin/python

import domashSystem as system
import zmq

config = system.config.default()
address = config.value('address')

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(address)

socket.send_json("exit")
r = socket.recv_json()
print r


