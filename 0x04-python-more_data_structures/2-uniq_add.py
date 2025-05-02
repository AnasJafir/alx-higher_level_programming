#!/usr/bin/python3
#from functools import reduce
def uniq_add(my_list=[]):
    '''new_list = list(set(my_list))
    result = reduce(lambda x,y : x+y, new_list)
    return result'''
    new_list = list(set(my_list))
    result = 0
    for i in new_list:
        result += i
    return result
