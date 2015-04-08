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


endc = '\033[0m'

bold = '\033[1m'
shadow = '\033[2m'
normal = '\033[3m'
underline = '\033[4m'
flash = '\033[5m'
reverse = '\033[7m'

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
purple = '\033[34m'
pink = '\033[35m'
blue = '\033[36m'
white = '\033[37m'

onred = '\033[41m'
ongreen = '\033[42m'
onyellow = '\033[43m'
onblue = '\033[44m'
onpurple = '\033[45m'
onlightblue = '\033[46m'
onwhite = '\033[47m'

l_red = '\033[91m'
l_green = '\033[92m'
l_yellow = '\033[93m'
l_purple = '\033[94m'
l_pink = '\033[95m'
l_blue = '\033[96m'
l_white = '\033[97m'

l_onred = '\033[101m'
l_ongreen = '\033[102m'
l_onyellow = '\033[103m'
l_onblue = '\033[104m'
l_onpurple = '\033[105m'
l_onlightblue = '\033[106m'
l_onwhite = '\033[107m'

	
def exception(plugin, description, suggestion):
	print red + bold + flash + 'Exception from file: ' +  endc + red + bold + plugin + '! ' +'Description: ' + description + '. Suggestion: ' + suggestion + '.' + endc 

def warning(plugin, description):
	print bold + yellow + 'Warning from file: ' + plugin + '! Description: ' + description + '.' + endc

def printf(text, *args):
	message = ''
	for arg in args:
		try:
			message += eval(arg) 
		except:
			exception(__name__, 'printf() does not accept argument \'' + arg + '\'', 'See domashMeta/output.py for legal arguments')
	print message + text + endc




