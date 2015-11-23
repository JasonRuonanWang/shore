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

void shorePut(char const *doid, char const *column, unsigned int rowid, unsigned int *shape, void *data){
    if(!isShoreClientCyInited) shoreClientCyInit();
    shorePutCy(doid, column, rowid, shape, data);
}

void shoreClientCyFinalise(){
    Py_Finalize();
}

