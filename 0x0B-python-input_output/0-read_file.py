#!/usr/bin/python3
"""Read a file Module"""


def read_file(filename=""):
    """Method to read a file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read())
