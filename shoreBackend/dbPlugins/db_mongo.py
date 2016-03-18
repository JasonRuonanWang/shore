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


import sys
sys.path.append('shoreBackend/filesPlugins')
from db import db
from pymongo import MongoClient
import numpy as np
import cPickle as pickle


class db_mongo(db):

    def __init__(self, event, config):
        db.__init__(self, event, config)
        client = MongoClient()
        self.__db = client.shore

    def read(self, msg):
        query_dict = {
            'doid':msg['doid'],
            'column':msg['column'],
        }
        msg['data'] = np.ndarray([msg['rows']] + msg['shape'], msg['datatype'])
        for i in range(0, msg['rows']):
            query_dict['row'] = i + msg['row']
            for record in self.__db['data'].find(query_dict):
                msg['data'][i,:] = pickle.loads(str(record['data']))

    def write(self, msg):
        query_dict = {
            'doid':msg['doid'],
            'column':msg['column'],
        }
        for i in range(0, msg['rows']):
            query_dict['row'] = i + msg['row']
            update_dict = {
                'data':pickle.dumps(msg['data'][i,:])
            }
            self.__db['data'].update(query_dict,{'$set':update_dict},upsert=True)

def get_class():
    return db_mongo

