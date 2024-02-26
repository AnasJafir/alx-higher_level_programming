#!/usr/bin/python3
"""Read a file Module"""


def read_file(filename=""):
    """Method to read a file"""
    with open(filename, "r", encoding="UTF-8") as file:
        print(file.read())
