#!/usr/bin/python3
"""Look up Module"""


def lookup(obj):
    """
    Method that returns a list of attributes
    and methods of a class
    """
    lst = dir(obj)
    return lst
