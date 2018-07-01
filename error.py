#!/usr/bin/python
# -*- coding:utf-8 -*-
try:
    f = open('1.txt')
    line = f.read(2)
    num = int(line)
    print "read num=%d" %num
except IOError,e:
    print "catch Error",e
except ValueError,e:
    print "catch Error",e
else:
    print "no error"
finally:
    try:
        print "close file"
        f.close()
    except Exception,e:
        print "catch errror"
#print "exec over"