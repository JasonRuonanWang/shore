#!/usr/bin/python

import shoreClient

shoreClient.shoreZmqInit()
ret=shoreClient.shoreGet("bbbk","data_Bool",0, 50)
print ret
print ret['data'].shape

