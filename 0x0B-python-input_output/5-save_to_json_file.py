#!/usr/bin/python3
"""Object to json file Module"""
import json


def save_to_json_file(my_obj, filename):
    """
    Method that saves JSON representation
    of an object into a json file
    """
    with open(filename, "w") as json_file:
        json.dump(my_obj, json_file)
