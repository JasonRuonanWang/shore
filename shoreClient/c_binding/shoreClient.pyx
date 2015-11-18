import sys
sys.path.append('../')
import client

cdef public void shorePut(const char *doid, const char* column, unsigned int rowid, unsigned int *dim, void *data):
    client.shorePut()

