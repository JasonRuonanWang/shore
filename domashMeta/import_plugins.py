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
sys.path.append('../domashMeta')
import output


DEBUG = True

# obtain the plugin category name in a string
category_name =  __file__.split('/')[-2].lower()[0:-7]
# define the plugin dictionary
__plugin_dict__ = {}

# obtain the plugin category name in a string
category_name =  __file__.split('/')[-2].lower()[0:-7]

# obtain the list of plugin files
__files__ = glob('{0}/{1}_*.py'.format(os.path.abspath(__path__[0]), category_name))
for _pc in __files__:
    # obtain the plugin file name
    plugin_filename = os.path.splitext(os.path.basename(_pc))[0]
    # obtain the plugin name
    plugin_name = plugin_filename.split('_')[1].lower()
    # import the plugin as a module

    if DEBUG:
        plugin_module = __import__('{0}.{1}'.format(__name__, plugin_filename), fromlist=[__name__])
        # define the object of the plugin instance, using the plugin name as the object name
        exec(plugin_name + '= plugin_module.get_class()')
        # register the object with the dictionary
        __plugin_dict__.update({plugin_name:eval(plugin_name)})
        # done
        output.printf("|- " + plugin_filename + " imported.", 'l_yellow')

    else:
        try:
            plugin_module = __import__('{0}.{1}'.format(__name__, plugin_filename), fromlist=[__name__])
            # define the object of the plugin instance, using the plugin name as the object name
            exec(plugin_name + '= plugin_module.get_class()')
            # register the object with the dictionary
            __plugin_dict__.update({plugin_name:eval(plugin_name)})
            # done
            output.printf("|- " + plugin_filename + " imported.", 'l_yellow')
        except:
            output.exception(__file__,"Failed to import plugin {0}".format(plugin_filename),"Check dependent libraries")





