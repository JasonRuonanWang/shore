default:static install

install:
ifdef LIBPATH
	mkdir -p $(LIBPATH)/shoreClient/include
	mkdir -p $(LIBPATH)/shoreClient/lib
	cp libShoreClient.so libShoreClient.a $(LIBPATH)/shoreClient/lib
	cp shoreClient.h $(LIBPATH)/shoreClient/include
endif

lib: cl
	cython *.pyx
	cc -fPIC *.c -lpython2.7 --shared -o libShoreClient.so

static:
	cython *.pyx
	cc -c -fPIC *.c -lpython2.7
	ar rcs libShoreClient.a *.o

cl:
	rm -rf *.so *.o *.a

clean:cl
	rm -rf shoreClientCy.c shoreClientCy.h
