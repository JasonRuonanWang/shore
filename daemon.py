#!/usr/bin/python

import domashSystem as system
import domashInfra as infra
import sys
sys.path.append('domashMeta')
import output

try:
	config = system.config.default
	socket = infra.socket.zmq

	address = config.get_address()
	socket.bind(address)

except:
	output.exception(__file__, "Compulsory plugins failed to load", "Please check dependent libraries")



