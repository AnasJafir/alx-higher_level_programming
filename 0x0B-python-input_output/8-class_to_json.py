#!/usr/bin/python3
"""
8-class_to_json module
"""


def class_to_json(obj):
    """
    class_to_json - returns the dictionary description with simple data structure
    Args:
        obj: instance of a class
    Return: the dictionary description with simple data structure
    """
    return obj.__dict__
