#!/usr/bin/python3
"""
Module to add two integers
a and b must be casted to int
"""


def add_integer(a, b=98):
    """ function adds a and b
    Returns: the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
            a = int(a)
    if isinstance(b, float):
            b = int(b)
    return a + b
