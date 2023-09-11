#!/usr/bin/python3
def no_c(my_string):
    list_of_chars = list(my_string)
    for char in list_of_chars:
        if char == 'c' or char == 'C':
            list_of_chars.remove(char)
    return("".join(list_of_chars))
