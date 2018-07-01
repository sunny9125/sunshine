#! /usr/bin/python
# -*- coding:utf-8 -*-


def dec(func):
    print ('call dec ')
    def in_dec(*arg):
        print ('in in_dec arg=',arg)
        if len(arg) == 0:
            return 0
        for var in arg:
            if not isinstance(var, int):
                return 0
        return func(*arg)
    return in_dec


@dec
def my_sum(*arg):
    print ('in my_sum,arg is',arg)
    if len(arg) == 0:
        return 0
    for var in arg:
        if not isinstance(var,int):
            return 0
    return sum(arg)


@dec
def my_average(*arg):
    if len(arg) == 0:
        return 0
    for var in arg:
        if not isinstance(var,int):
            return 0
    return sum(arg)/len(arg)



#my_sum = indec(my_sum)
#my_sum = dec(my_sum)
#my_average = dec(my_average)
print (my_sum(1,2,3,4,5))
#print (my_sum(1,2,3,4,5,'6'))
#print (my_average(1,2,3,4,5))
#print (my_average())


"""
装饰器用来装饰函数
返回一个函数对象
被装饰函数标识符指向返回的函数对象
语法糖：@deco
"""