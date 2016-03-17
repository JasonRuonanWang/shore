import shoreClient

shoreClient.shoreZmqInit()
ret = shoreClient.shoreQuery("aaa","data_Complex",0)

ret = shoreClient.shoreQuery("aaa")

print 'Data Object ******************** '
for i in ret['return']['do']:
    print i, ret['return']['do'][i]

'''

print 'Column ****************** '
for i in ret['return']['column']:
    print i, ret['return']['column'][i]
    '''
