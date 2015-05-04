#!/usr/bin/python

import sys
sys.path.append('../../domashMeta')
import output
sys.path.append('../../domashSystem/workflowPlugins/')
from workflow_list import workflow_list

print workflow_list().get_previous('request')
print workflow_list().get_previous('db')
print workflow_list().get_previous('storage')


