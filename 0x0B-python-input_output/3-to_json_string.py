#!/usr/bin/python3
"""
3-to_json_string module
"""
import json


def to_json_string(my_obj):
    """
    to_json_string - returns the json representation
    Args:
        my_obj: the object to represent (string)
    Return: the JSON representation
    """
    return json.dumps(my_obj)
