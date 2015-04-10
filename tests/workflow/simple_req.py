#!/usr/bin/python

import zmq


context = zmq.Context(10)
socket = context.socket(zmq.REQ)
socket.connect('tcp://180.149.250.157:12306')

while True:
	socket.send('aa')
	r = socket.recv()

