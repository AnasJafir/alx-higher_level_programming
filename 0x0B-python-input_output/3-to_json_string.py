#!/usr/bin/python3
"""JSON representation of a string Module"""
import json


def to_json_string(my_obj):
    """Method that returns the JSON representation of a string"""
    json_string = json.dumps(my_obj)
    return json_string
