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
#    Any bugs, problems, and/or suggestions please email to
#    jason.wang@icrar.org or jason.ruonan.wang@gmail.com


from db import db
from pymongo import MongoClient
from bson.objectid import ObjectId
import gridfs
import numpy as np
import cPickle as pickle
import bson


class db_gridfs(db):

    def __init__(self, event, config):
        db.__init__(self, event, config)
        client = MongoClient(self.config('db_address'))
        self.__db = client.shoreGridFS
        self.__fs = gridfs.GridFS(self.__db)

    def read(self, msg):
        msg['data'] = np.ndarray([msg['rows']] + msg['shape'], msg['datatype'])
        for i in range(0, msg['rows']):
            cursor = self.__db.fs.files.find({'doid':msg['doid'], 'column':msg['column'], 'row':msg['row']})
            msg['data'][i,:]= pickle.loads(self.__fs.get(ObjectId(cursor[0]['_id'])).read())
        return True

    def write(self, msg):
        for i in range(0, msg['rows']):
            self.__fs.put(pickle.dumps(msg['data'][i,:]), doid=msg['doid'], column=msg['column'], row = msg['row']+i)
        return True

def get_class():
    return db_gridfs

