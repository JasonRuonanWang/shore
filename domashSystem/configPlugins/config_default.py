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

import sys
sys.path.append('domashMeta')
import output



class config_default:

	__config_dict__ = {}

	def __init__(self):
		try:
			config_file = open('config','r')
			for line in config_file.readlines():
				try:
					left = line.split('=')[0]
					right = line.split('=')[1].split('\n')[0]
					self.__config_dict__.update({left:right})
				except:
					continue
		except:
			output.exception(__name__,'Cannot find config file','Check if config file is in domash root directory')



	def get_address(self):
		try:
			return self.__config_dict__['address']
		except:
			return

	def print_dict():
		print __config_dict__


def instantiate():
	return config_default()




