#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        big_i = my_list[0]
        for i in my_list:
            if i > big_i:
                big_i = i
        return big_i
    return None
