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

import domashInfra as infra
import domashSystem as system
import sys
sys.path.append('domashMeta')
import output


config = system.config.default()
config.print_dict()
event = eval("system.event.{0}()".format(config.value('event')))
mainloop = eval("system.mainloop.{0}()".format(config.value('mainloop')))


address = config.value('address')
event.bind(address)

event.reg_on_recv(mainloop.getfunc())
event.start()




