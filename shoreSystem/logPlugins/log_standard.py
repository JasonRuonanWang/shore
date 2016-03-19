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

from log import log
import time

class log_standard(log):

    def log_func(self,msg):
        text = self.style_code['shadow'] + '[' + time.strftime("%a, %d %b %Y %H:%M:%S") + '] '
        if 'source' in msg:
            if msg['source']:
                text += 'From ' + msg['source'] + ' '
        text += self.style_code['endc']
        if 'category' in msg:
            if msg['category']:
                if msg['category'] == 'system':
                    text += self.style_code['pink'] + '<SYSTEM> '
                elif msg['category'] == 'error':
                    text += self.style_code['red'] + '<ERROR> '
                elif msg['category'] == 'warning':
                    text += self.style_code['yellow'] + '<WARNING> '
            else:
                text += self.style_code['blue'] + '<EVENT> '

        if 'color' in msg:
            if msg['color']:
                text += self.style_code[msg['color']]
        if 'style' in msg:
            if msg['style']:
                text += self.style_code[msg['style']]
        if 'text' in msg:
            text += msg['text']
        text += self.style_code['endc']
        print (text)


def get_class():
    return log_standard


