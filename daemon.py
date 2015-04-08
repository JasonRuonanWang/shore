#!/usr/bin/python
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

import domashSystem as system
import domashInfra as infra
import sys
sys.path.append('domashMeta')
import output


try:
	config = system.config.default()
	socket = eval("system.socket.{0}()".format(config.socket()))
	event = eval("system.event.{0}()".format(config.event()))

	address = config.address()
	socket.bind(address)

except:
	output.exception(__file__, "Compulsory plugins failed to load", "Please check dependent libraries")



