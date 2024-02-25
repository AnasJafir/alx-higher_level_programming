#!/usr/bin/python3
"""Same object Module"""


def is_same_class(obj, a_class):
    """
    Method returns True if the object is an instance of a_class
    Otherwise, it returns False
    """
    return obj.__class__ == a_class
