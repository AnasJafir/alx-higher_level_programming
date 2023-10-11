#!/usr/bin/python3
"""
101-add_attribute module
"""


def add_attribute(obj, name, value):
    """function to check if an attribute can be set"""

    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    elif hasattr(obj, "__slots__") and name in obj.__slots__:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
