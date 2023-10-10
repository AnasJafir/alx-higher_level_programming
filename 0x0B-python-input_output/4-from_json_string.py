#!/usr/bin/python3
"""
4-from_json_string module
"""
import json


def from_json_string(my_str):
    """
    from_json_string - returns an object represented by json
    Args:
        my_str: json representation
    Return: the object
    """
    return json.loads(my_str)
