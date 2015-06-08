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


class log_default(log):

    def exception(self,msg):
        text = ''
        if msg.has_key('file'):
            text = self.red + self.bold + self.flash + 'Exception from: ' + msg['file'] + '! ' + self.endc
        if msg.has_key('description'):
            text += self.red + self.bold + 'Description: ' + msg['description'] + '.' + self.endc
        if msg.has_key('suggestion'):
            text += self.red + self.bold + 'Suggestion: ' + msg['suggestion'] + '.' + self.endc
        print text

    def warning(self,msg):
        text = ''
        if msg.has_key('file'):
            text = self.yellow + self.bold + self.flash + 'Warning from: ' + msg['file'] + '! ' + self.endc
        if msg.has_key('description'):
            text += self.red + self.bold + 'Description: ' + msg['description'] + '.' + self.endc
        if msg.has_key('suggestion'):
            text += self.red + self.bold + 'Suggestion: ' + msg['suggestion'] + '.' + self.endc
        print text

    def printf(self,msg):
        if msg.has_key('color'):
            text = eval('self.{0}'.format(msg['color']))
        if msg.has_key('text'):
            text += msg['text']
        text += self.endc
        print text


def get_class():
    return log_default


