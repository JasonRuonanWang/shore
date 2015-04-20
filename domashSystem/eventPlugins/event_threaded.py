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

import zmq 
import sys
sys.path.append('../domashMeta')
import output
import threading




class event:

	__isbound__ = None
	__on_recv__ = None
	__clients__ = None
	__workers__ = None
	__url_workers__ = "inproc://workers"
	__url_clients__ = ""

	def worker_routine(self, context=None):
		context = context or zmq.Context.instance()
		socket = context.socket(zmq.REP)
		socket.connect(self.__url_workers__)

		while True:
			msg  = socket.recv()
			self.__on_recv__(msg)
			socket.send("OK")

	def __del__(self):
		if self.__isbound__:
			self.unbind()

	def bind(self, address):

		self.__url_clients__ = address

		while True:

			context = zmq.Context.instance()

			self.__clients__ = context.socket(zmq.ROUTER)
			self.__workers__ = context.socket(zmq.DEALER)

			try:
				self.__clients__.bind(self.__url_clients__)
				self.__workers__.bind(self.__url_workers__)
				self.__isbound__ = True
				output.printf('bound {0}'.format(self.__url_clients__),'blue')
				return

			except:
				output.exception(__name__,'unable to bind address {0}'.format(self.__url_clients__),'')
				self.__url_clients__ = raw_input('please re-enter the local address:')

	def unbind(self):
		try:
			self.socket.unbind(self.__url_clients__)
			self.__isbound__ = False 
			output.printf('unbound {0}'.format(self.__url_clients__),'blue')
		except:
			output.exception(__name__,'unable to unbind address'.format(self.__url_clients__),'')

	def start(self):

		for i in range(1):
			thread = threading.Thread(target=self.worker_routine, args=())
			thread.start()

		zmq.device(zmq.QUEUE, self.__clients__, self.__workers__)

	def reg_on_recv(self, func):
		self.__on_recv__ = func


def instantiate():
	return event


