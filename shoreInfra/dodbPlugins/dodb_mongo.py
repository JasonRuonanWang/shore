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

import sys
sys.path.append('shoreInfra/dodbPlugins')
from dodb import dodb
from pymongo import MongoClient

class dodb_mongo(dodb):

    __db = None

    def init_db(self):
        if not self.__db:
            client = MongoClient()
            self.__db = client.shore

    def update_do(self, msg):
        self.init_db()
        self.__db.do.update(
                {'doid':msg['doid']},
                {
                    '$max':{'rows':msg['row']},
                    '$addToSet':{'columns':msg['column']}
                    },
                upsert=True
                )

    def update_column(self, msg):
        self.init_db()
        msg['datatype'] = self.dtype_shore_to_numpy[msg['datatype']]
        cursor = self.__db.column.find({'doid':msg['doid'], 'column':msg['column']})
        if cursor.count() == 0:
            print msg['doid'], msg['column'], msg['shape'], msg['datatype']
            self.__db.column.insert_one({'doid':msg['doid'], 'column':msg['column'], 'shape':msg['shape'], 'datatype':msg['datatype'].__name__ })
        else:
            if cursor[0]['shape'] != msg['shape']:
                self.__db.column.update({'doid':msg['doid'], 'column':msg['column']}, {'$set':{'shape':None}})
        if cursor.count() > 1:
            self.log('Warning: Data Object {0} Column {1} has multiple records in dodb.column'.format(msg['doid'],msg['column']), category='warning', source=__name__)

    def query_do(self, msg):
        self.init_db()
        cursor = self.__db.do.find({'doid':msg['doid']})
        if cursor.count() == 0:
            return None
        else:
            if cursor.count() > 1:
                self.log('Warning: Data Object {0} has multiple records in dodb.do'.format(msg['doid']), category='warning', source=__name__)
#            print cursor[0]
#            print type(cursor[0])

    def query_column(self, msg):
        self.init_db()
        return

    def query_row(self, msg):
        self.init_db()
        return

def get_class():
    return dodb_mongo

