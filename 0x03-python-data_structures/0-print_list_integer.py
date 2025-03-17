#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for x in my_list:
        if type(x) != int:
            raise TypeError("my_list must contain only integers")
        print(x)
