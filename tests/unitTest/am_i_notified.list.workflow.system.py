#!/usr/bin/python

import sys
sys.path.append('../../domashMeta')
import output
sys.path.append('../../domashSystem/workflowPlugins/')
from workflow_list import workflow_list

print workflow_list().am_i_notified(current = 'db', last = 'request')
print workflow_list().am_i_notified('storage','request')
print workflow_list().am_i_notified('storage','db')


