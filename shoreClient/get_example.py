import shoreClient

shoreClient.shoreZmqInit()
ret=shoreClient.shoreGet("eeef","data_DComplex",0, 50)
print ret
print ret['data'].shape
