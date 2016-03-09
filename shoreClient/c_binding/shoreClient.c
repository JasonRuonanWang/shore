//    (c) University of Western Australia
//    International Centre of Radio Astronomy Research
//    M468/35 Stirling Hwy
//    Perth WA 6009
//    Australia
//
//    Copyright by UWA,
//    All rights reserved
//
//    This library is free software; you can redistribute it and/or
//    modify it under the terms of the GNU Lesser General Public
//    License as published by the Free Software Foundation; either
//    version 2.1 of the License, or (at your option) any later version.
//
//    This library is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
//    Lesser General Public License for more details.
//
//    You should have received a copy of the GNU Lesser General Public
//    License along with this library; if not, write to the Free Software
//    Foundation, Inc., 59 Temple Place, Suite 330, Boston,
//    MA 02111-1307  USA
//
//    Any bugs, problems, and/or suggestions please email to
//    jason.wang@icrar.org or jason.ruonan.wang@gmail.com


#include <stdbool.h>
#include <Python.h>
#include "shoreClient.h"
#include "shoreClientCy.h"

void shoreClientCyInit(){
    Py_Initialize();
    initshoreClientCy();
    shoreZmqInitCy();
    isShoreClientCyInited = true;
}

void shorePut(const char *doid, const char *column, const unsigned int rowid, const unsigned int rows, const unsigned int *shape, const int dtype, const void *data){
    if(!isShoreClientCyInited) shoreClientCyInit();
    shorePutCy(doid, column, rowid, rows, shape, dtype, data);
}

int shoreQuery(const char *doid, const char *column, const unsigned int rowid, unsigned int *shape, int *dtype){
    if(!isShoreClientCyInited) shoreClientCyInit();
    shoreQueryCy(doid, column, rowid, shape, dtype);
    return 0;
}

void shoreGet(const char *doid, const char *column, const unsigned int rowid, const unsigned int rows, unsigned int *shape, int *dtype, void *data){
    if(!isShoreClientCyInited) shoreClientCyInit();
    shoreGetCy(doid, column, rowid, rows, shape, dtype, data);
}

void shoreClientCyFinalise(){
    Py_Finalize();
    isShoreClientCyInited = false;
}


