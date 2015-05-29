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

import shoreSystem as system
import shoreInfra as infra
import shoreBackend as backend
import sys
sys.path.append('shoreMeta')
import output

def start_daemon():
    config = system.config.default()
    config.print_dict()
    address = config.value('address')
    event = eval("system.event.{0}(address)".format(config.value('event')))

    for category in infra.plugin_dict:
        confv = config.value(category)
        for plugin in infra.plugin_dict[category]:
            if plugin == confv:
                instance = eval("infra.{0}.{1}(event)".format(category, plugin))
                output.printf('Plugin {0}.{1} instantiated and registered into the event loop.'.format(category, plugin), 'yellow')


    for category in backend.plugin_dict:
        for plugin in backend.plugin_dict[category]:
            instance = eval("backend.{0}.{1}(event)".format(category, plugin))
            output.printf('Plugin {0}.{1} instantiated and registered into the event loop.'.format(category, plugin), 'yellow')


    event.start()

if __name__ == "__main__":
    start_daemon()


