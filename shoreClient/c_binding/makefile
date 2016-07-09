CC=gcc-4.9

default:dynamic install

install:
ifdef LIBPATH
	mkdir -p $(LIBPATH)/shoreClient/include
	mkdir -p $(LIBPATH)/shoreClient/lib
	cp libShoreClient.* $(LIBPATH)/shoreClient/lib
	cp shoreClient.h $(LIBPATH)/shoreClient/include
endif

object:
	$(CC) -fPIC -c *.c -lpython2.7

cython:
	cython *.pyx

dynamic: cl cython
	$(CC) -fPIC *.c -lpython2.7 --shared -o libShoreClient.so

static: cl cython
	$(CC) -c -fPIC *.c -lpython2.7
	ar rcs libShoreClient.a *.o

cl:
	rm -rf *.so *.o *.a

clean:cl
	rm -rf shoreClientCy.c shoreClientCy.h
