#ifdef __APPLE__
#include <OpenCL/opencl.h>
#else
#include <CL/cl.h>
#endif

#include <shoreClient.h>
#include "shoreClientCl.h"

cl_context clContext;
cl_command_queue clQueue;



int shorePutCl(const char *doid, const char *column, const unsigned int rowid, const unsigned int rows, const unsigned int *shape, const int dtype, const cl_mem *data){
    return shorePut(doid, column, rowid, rows, shape, dtype, data);
}

int shoreGetCl(const char *doid, const char *column, const unsigned int rowid, const unsigned int rows, cl_mem data){

    unsigned int shape[10];
    int dtype[1];

    unsigned int rows_returned[1];
    shoreQuery(doid, column, rows_returned, shape, dtype);
    int i;
    int nelements=rows;
    for (i=0; i<shape[0]; i++){
        nelements *= shape[i];
    }

    int nbytes = nelements;
    switch (dtype[0]){
        case shoreTypeBool:
            nbytes *= sizeof(bool);
        case shoreTypeChar:
            nbytes *= sizeof(char);
        case shoreTypeUChar:
            nbytes *= sizeof(unsigned char);
        case shoreTypeShort:
            nbytes *= sizeof(short);
        case shoreTypeUShort:
            nbytes *= sizeof(unsigned short);
        case shoreTypeInt:
            nbytes *= sizeof(int);
        case shoreTypeUInt:
            nbytes *= sizeof(unsigned int);
        case shoreTypeFloat:
            nbytes *= sizeof(float);
        case shoreTypeDouble:
            nbytes *= sizeof(double);
        case shoreTypeComplex:
            nbytes *= sizeof(float)*2;
        case shoreTypeDComplex:
            nbytes *= sizeof(double)*2;
    }

    void *buffer = malloc(nbytes);

    shoreGet(doid, column, rowid, rows, buffer);

	clEnqueueWriteBuffer(clQueue, data, CL_TRUE, 0, nbytes, buffer, 0,0,0);

    return shoreGet(doid, column, rowid, rows, data);
}

