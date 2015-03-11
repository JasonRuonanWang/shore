#!/usr/bin/python

import sys
sys.path.append('../domashMeta')
import output

output.exception('unitTest', 'Just a test', 'No action needed')
output.warning('unitTest', 'Just a test')

output.superprint('Test printing in red', 'onred', 'flash')
output.superprint('Test printing in red', 'daga')



