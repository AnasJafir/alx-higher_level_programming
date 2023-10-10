#!/usr/bin/python3
"""Module containing a function that
reads a file an prints it to stdout
"""


def read_file(filename=""):
    """Function that reads a file and prints it"""
    try:
        with open("my_file_0.txt", mode="r", encoding="utf-8") as f:
            print(f.read(), end='')
    except FileNotFoundError:
        print("file doesn't exist")
    except PermissionError:
        print("file permission")
