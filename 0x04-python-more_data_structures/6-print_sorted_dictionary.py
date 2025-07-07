#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_dictionary = {}
    sorted_keys = sorted(a_dictionary)
    for i in sorted_keys:
        new_dictionary[i] = a_dictionary[i]
    for key in new_dictionary:
        print(key+':',new_dictionary[key])
