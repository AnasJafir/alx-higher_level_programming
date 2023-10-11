#!/usr/bin/python3
"""
3-is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - checks if
    if the object is an instance of the specified class
    or if the object is an instance of a class that inherited from
    Args:
        obj: the object
        a_class: the class
    Return: True or False
    """
    return isinstance(obj, a_class)
