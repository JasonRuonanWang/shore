install:lib

ifdef LIBPATH
	cp libShoreClient.so $(LIBPATH)/shoreClient/lib 
	cp shoreClient.h $(LIBPATH)/shoreClient/include
	cp ../shoreClient.py $(LIBPATH)/shoreClient/python
endif

lib: cl
	cython *.pyx
	cc -fPIC *.c -lpython2.7 --shared -o libShoreClient.so

cl:
	rm -rf *.so *.o

clean:cl
	rm -rf shoreClientCy.c shoreClientCy.h
