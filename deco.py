#! /usr/bin/python
# -*- coding:utf-8 -*-


def deco(func):
    def in_deco(x,y):  #若bar有参数，此处必须有参数
        print ('in deco')
        func(x,y)
    print ('call deco')
    return in_deco #内建函数必须有返回值


@deco
def bar(x,y):
    print ('in bar',x+y)
print (type(bar))
bar(1,2)