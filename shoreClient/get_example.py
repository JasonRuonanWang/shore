import shoreClient

shoreClient.shoreZmqInit()
ret=shoreClient.shoreGet("eeef","data_Bool",0, 50)
print ret
print ret['data'].shape

ret=shoreClient.shoreGet("eeef","data_uChar",0, 50)
print ret
print ret['data'].shape
