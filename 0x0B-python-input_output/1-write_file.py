#!/usr/bin/python3
"""Write in a file Module"""


def write_file(filename="", text=""):
    """Method to write in a file"""
    with open(filename, "w", encoding='utf-8') as f:
        chars_count = f.write(text)
    return chars_count
