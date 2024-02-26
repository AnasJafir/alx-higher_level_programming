#!/usr/bin/python3
"""From JSON to abject Module"""
import json


def from_json_string(my_str):
    """Method that returns object represented by JSON string"""
    return json.loads(my_str)
