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

from dodb import dodb
from pymongo import MongoClient

class dodb_mongo(dodb):

    __db = None

    def __init__(self, event, config):
        dodb.__init__(self, event, config)
        client = MongoClient()
        self.__db = client.shore

    def db_query(self, collection, query_dict):
        ret = []
        for i in self.__db[collection].find(query_dict):
            ret.append(i)
        return ret

    def db_update(self, collection, query_dict, update_dict, operation):
        if operation == 'set':
            self.__db[collection].update_many(query_dict,{'$set':update_dict},upsert=True)
        elif operation == 'max':
            self.__db[collection].update_many(query_dict,{'$max':update_dict},upsert=True)
        elif operation == 'add':
            self.__db[collection].update_many(query_dict,{'$addToSet':update_dict},upsert=True)

    def db_insert(self, collection, insert_dict):
        self.__db[collection].insert_one(insert_dict)

    def db_delete(self, collection, delete_dict):
        self.__db[collection].delete_many(delete_dict)

    def update(self, msg):
        self.__db.do.update(
                {'doid':msg['doid']},
                {
                    '$max':{'total_rows':(msg['row']+msg['rows'])},
                    '$addToSet':{'columns':msg['column']}
                    },
                upsert=True
                )
        cursor = self.__db.column.find({'doid':msg['doid'], 'column':msg['column']})
        if cursor.count() == 0:
            self.__db.column.insert_one({'doid':msg['doid'], 'column':msg['column'], 'shape':msg['shape'], 'datatype':str(msg['datatype']), 'backend':msg['backend']})
        else:
            if cursor[0]['shape'] != msg['shape']:
                self.log('Data Object {0} Column {1} shape does not match. Did not touch dodb.'.format(msg['doid'],msg['column']), category='warning', source=__name__)
        if cursor.count() > 1:
            self.log('Data Object {0} Column {1} has multiple records in dodb.column'.format(msg['doid'],msg['column']), category='warning', source=__name__)

def get_class():
    return dodb_mongo

