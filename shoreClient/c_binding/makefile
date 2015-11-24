install:lib
ifdef LIBPATH
	cp libShoreClient.so $(LIBPATH)/shoreClient/lib 
	cp shoreClient.h $(LIBPATH)/shoreClient/include
	cp ../shoreClient.py $(LIBPATH)/shoreClient/python
endif

lib:
	cython *.pyx
	cc -std=c99 *.c -lpython2.7 --shared -o libShoreClient.so

cl:
	rm -rf *.so *.o

clean:cl
	rm -rf *.c *.h
