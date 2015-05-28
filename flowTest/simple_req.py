#!/usr/bin/python

import zmq
import json


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://180.149.250.157:12306')

msg = {}
msg['operation'] = 'query'

socket.send_json(msg)
r = socket.recv_json()
print r


