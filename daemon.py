#!/usr/bin/python

import domashSystem as system
import domashInfra as infra

config = system.config.default
socket = infra.socket.zmq

address = config.get_address()
socket.bind(address)




