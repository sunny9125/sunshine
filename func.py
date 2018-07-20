#!/usr/bin/python
# -*- coding:utf-8 -*-

def func_100(val):
    passline = 60
    if val >= passline:
        print ('%d pass'%val)
    else:
        print ('failed')


def func_150(val):
    passline = 90
    if val >= passline:
        print ('%d pass'%val)
    else:
        print ('failed')

def set_passline(passline): #passline=60
    def cmp(val):
        if val >= passline: #cmp为闭包
            print ('pass')
        else:
            print ('failed')
    return cmp

f_100 = set_passline(60)
f_150 = set_passline(90)
f_100(89)
f_150(89)

'''
闭包的作用：
封装
代码的复用
'''