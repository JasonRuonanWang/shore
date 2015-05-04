#!/usr/bin/python

import zmq
import json


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://180.149.250.157:12306')


socket.send_json({'operation':'test', 'status':'pre', 'module':'request'})
r = socket.recv()
print r
s = json.loads(r)

print type(s)
print s


