#!/usr/bin/python

import zmq


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect('tcp://180.149.250.157:12306')

socket.send("exit")
r = socket.recv()
print r


