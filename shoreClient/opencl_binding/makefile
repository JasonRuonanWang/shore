PLATFORM=$(shell uname -s)

ifeq ($(PLATFORM),Darwin)
  LDLIBS=-framework OpenCL
else
  LDLIBS=-lOpenCL
endif

ifeq ($(PLATFORM),Linux)
  LDLIBS += -ldl
endif


all:
	cc *.c --shared -o shoreClientCl.so $(LDLIBS) -lshoreClient
