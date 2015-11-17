PYINC=-I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7
PYLIB=-L/System/Library/Frameworks/Python.framework/Versions/2.7/lib

a:
	cython *.pyx
	cc *.c $(PYINC) $(PYLIB) -lpython2.7 --shared -o libShoreClient.so

cl:
	rm -rf *.so *.o
