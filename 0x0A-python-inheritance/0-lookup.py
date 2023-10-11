#!/usr/bin/python3
"""
0-lookup module
"""


def lookup(obj):
    """
    lookup - returns the list of attributes of an object
    Args:
        obj : the object
    Return: list of attributes
    """
    return dir(obj)
