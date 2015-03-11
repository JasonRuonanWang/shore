#
#    (c) University of Western Australia
#    International Centre of Radio Astronomy Research
#    M468/35 Stirling Hwy
#    Perth WA 6009
#    Australia
#
#    Copyright by UWA,
#    All rights reserved
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston,
#    MA 02111-1307  USA
#
#	 Any bugs, problems, and/or suggestions please email to 
#	 jason.wang@icrar.org or jason.ruonan.wang@gmail.com

import sys
import zmq
sys.path.append('../domashMeta')
import output

class socket_zmq:

	address = None
	isbound = None

	def __del__(self):
		if self.isbound:
			self.unbind()

	def bind(self, address):

		self.address = address

		while True:
			try:
				self.context = zmq.Context(10)
				self.socket = self.context.socket(zmq.REP)
				self.socket.bind(self.address)
				self.isbound = True
				output.printf('bound {0}'.format(self.address),'blue')
				return self.socket
			except:
				output.exception(__name__,'unable to bind address'.format(self.address),'')
				self.address = raw_input('please re-enter the local address:')


	def unbind(self):
		try:
			self.socket.unbind(self.address)
			self.isbound = False 
			output.printf('unbound {0}'.format(self.address),'blue')
		except:
			output.exception(__name__,'unable to unbind address'.format(self.address),'')

	def send(self, msg_req):
		self.socket.send(msg_req)
		self.socket.receive(msg_rep)
	







def instantiate():
	return socket_zmq()



