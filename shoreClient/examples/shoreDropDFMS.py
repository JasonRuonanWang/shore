#
#    ICRAR - International Centre for Radio Astronomy Research
#    (c) UWA - The University of Western Australia, 2016
#    Copyright by UWA (in the framework of the ICRAR)
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

from dfms.drop import ShoreDROP
from dfms.apps.bash_shell_app import BashShellApp
import threading
from dfms.droputils import EvtConsumer
import numpy as np


doid = 'abc1046'
column = 'data'
row = 0
rows = 1

# Create the Drops
a = ShoreDROP(doid, doid, doid=doid, column=column, row=row, rows=rows)
b = BashShellApp('b', 'b', command="echo hello")
c = ShoreDROP(doid, doid, doid=doid, column='processed_data', row=row, rows=rows)

# Wire them together
b.addInput(a)
b.addOutput(c)

# The execution is asyncrhonously triggered by setCompleted()
# so we need to wait on an event that will be set when C moves to COMPLETED
# (or ERROR)
finished = threading.Event()
c.subscribe(EvtConsumer(finished), 'status')

# Fire and wait

rows = 1
xdim = 5
ydim = 10
data = np.ndarray([rows,xdim,ydim])
for r in range(rows):
    for x in range(xdim):
        for y in range(ydim):
            data[r][x][y] = x * 100 + y

a.write(data)
a.setCompleted() # This is the actual trigger
finished.wait(100)

desc = a.open()
print a.read(desc)
a.close(desc)

'''
# Read whatever is in C now
desc = c.open()
print c.read(desc)
c.close(desc)

'''
