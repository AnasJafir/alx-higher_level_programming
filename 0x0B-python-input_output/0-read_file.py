#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    read_file - function to read and print a file to stdout
    Args:
        filename: name of file
    """
    with open(filename, "r",  encoding="UTF-8") as f:
        print(f.read(), end="")
