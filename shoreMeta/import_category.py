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

from glob import glob
import os
import sys
sys.path.append('shoreMeta')
import output


# obtain the list of plugin category directories
__directories__ = glob('{0}/*Plugins'.format(os.path.abspath(__path__[0])))

__categories__ = []

plugin_dict = {}


for _pc in __directories__:
	# obtain the plugin category directory
	category_dirname = os.path.splitext(os.path.basename(_pc))[0]
	output.printf('Searching ' + category_dirname , 'bold', 'yellow')
	# import the plugin category as a module
	category_module = __import__('{0}.{1}'.format(__name__, category_dirname), fromlist=[__name__])
	# define the object of the plugin category instance
	exec(category_module.category_name + '= category_module')
	# register all plugins of this category with the dictionary
	plugin_dict.update({category_module.category_name:category_module.__plugin_dict__.keys()})
	__categories__.append(category_module.category_name)


def print_categories():
	print __categories__

def print_dictionary():
	print plugin_dict

def print_directories():
	print __directories__


