#!/usr/bin/python3
"""
4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
    inherits_from - checks if the object is
    an instance of a class that inherited
    Args:
        obj: the object
        a_class: the class
    Return: True or False
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
