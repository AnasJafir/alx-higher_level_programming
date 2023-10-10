#!/usr/bin/python3
"""
5-save_to_json_file module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - write an object to a file using json
    Args:
        filename: name of file
        my_obj: object to write to the file
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
