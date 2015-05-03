#!/usr/bin/python

import zmq
import json


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://180.149.250.157:12306')


socket.send_json(json.dumps({'operation':"just a test"}))
r = socket.recv()
print r
s = json.loads(r)
while type(s) != dict:
    s = json.loads(s)

print type(s)
print s


