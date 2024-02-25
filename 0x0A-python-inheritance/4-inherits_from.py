#!/usr/bin/python3
"""Inheritance Check Module"""


def inherits_from(obj, a_class):
    """
    Method that returns :
    True ifthe object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    Otherwise, False
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
