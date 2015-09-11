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

    def on_exception(self,msg):
        text = ''
        if msg.has_key('file'):
            text  = self.style_code['red']
            text += self.style_code['bold']
            text += self.style_code['flash']
            text += 'Exception from: ' + msg['file'] + '! '
            text += self.style_code['endc']
        if msg.has_key('description'):
            text += self.style_code['red']
            text += self.style_code['bold']
            text += 'Description: ' + msg['description'] + '.'
            text += self.style_code['endc']
        if msg.has_key('suggestion'):
            text += self.style_code['red']
            text += self.style_code['bold']
            text += 'Suggestion: ' + msg['suggestion'] + '.'
            text += self.style_code['endc']
        print text

    def on_warning(self,msg):
        text = ''
        if msg.has_key('file'):
            text  = self.style_code['yellow']
            text += self.style_code['bold']
            text += self.style_code['flash']
            text += 'Warning from: ' + msg['file'] + '! '
            text += self.style_code['endc']
        if msg.has_key('description'):
            text += self.style_code['yellow']
            text += self.style_code['bold']
            text += 'Description: ' + msg['description'] + '.'
            text += self.style_code['endc']
        if msg.has_key('suggestion'):
            text += self.style_code['yellow']
            text += self.style_code['bold']
            text += 'Suggestion: ' + msg['suggestion'] + '.'
            text += self.style_code['endc']
        print text

    def on_printf(self,msg):
        if msg.has_key('color'):
            text = self.style_code[msg['color']]
        if msg.has_key('style'):
            text += self.style_code[msg['style']]
        if msg.has_key('text'):
            text += msg['text']
        text += self.style_code['endc']
        if msg.has_key('source'):
            if msg['source'] is not '':
                text = 'From ' + msg['source'] + ':' + text
        print text


def get_class():
    return log_default


