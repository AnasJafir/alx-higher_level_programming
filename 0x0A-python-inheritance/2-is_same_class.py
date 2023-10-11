#!/usr/bin/python3
"""
2-is_same_class module
"""


def is_same_class(obj, a_class):
    """
    is_same_class - checks if an object is an
    instance of a class
    Args:
        obj: the object
        a_class: the class
    Return: True or False
    """
    return type(obj) is a_class
