import shoreClient

shoreClient.shoreZmqInit()
ret=shoreClient.shoreGet("aaa","data_Complex",0)
print ret
print len(ret)
