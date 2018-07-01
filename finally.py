#/usr/bin/python
# -*- coding:utf-8 -*-

try:
    f = open('1.txt')
    print int(f.read())
except:

finally:
    print "file close"
    f.close()