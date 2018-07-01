import os
try:
    f = open('1.txt')
    print "in try f.read():",f.read(2)
    f.seek(-5,os.SEEK_SET)
except IOError,e:
    print "catch IOError:",e
except ValueError,e:
    print "catch ValueError:",e
finally:
    f.close()
print "try-finally:",f.closed


try:
    with open('1.txt') as f1:
        print "in with f1.read:",f1.read(2)
        f.seek(-5,os.SEEK_SET)
except ValueError,e:
    print "in with catch ValueError:",e
    print "with :",f1.closed