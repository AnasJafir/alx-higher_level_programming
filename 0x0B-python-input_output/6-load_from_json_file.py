#!/usr/bin/python3
"""Load object from JSON file Module"""
import json


def load_from_json_file(filename):
    """Method that load object fron JSON file"""
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
