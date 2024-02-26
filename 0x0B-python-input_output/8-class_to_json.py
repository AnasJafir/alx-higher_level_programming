#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """
    Method that returns the dictionnary description of an object for
    JSON serialization
    """
    dct = obj.__dict__
    return dct
