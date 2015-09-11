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

from dodb import dodb
from pymongo import MongoClient

class dodb_mongo(dodb):

    __db = None

    def init_db(self):
        if not self.__db:
            client = MongoClient()
            self.__db = client.shore

    def query_do(self, doid):
        self.init_db()
        cursor = self.__db.do.find({'doid':doid})
        if cursor.count() == 0:
            return None
        elif cursor.count() == 1:
            return cursor[0]
        else:
            self.printf('Warning: Data Object {0} has multiple records in dodb'.format(doid), color='yellow', source=__name__)
            return cursor[0]

    def query_col(self, doid, column):
        self.init_db()
        return

    def query_row(self, doid, column, row):
        self.init_db()
        return


def get_class():
    return dodb_mongo

