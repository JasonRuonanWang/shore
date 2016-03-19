from shoreClient import shoreClient as shore
import sys


if len(sys.argv) == 2:
    ret = shore.shoreDelete(sys.argv[1])
    print ret

if len(sys.argv) == 3:
    ret = shore.shoreDelete(sys.argv[1], sys.argv[2])
    print ret


