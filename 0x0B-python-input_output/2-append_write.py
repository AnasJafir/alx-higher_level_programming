#!/usr/bin/python3
"""Append text to a text file Module"""


def append_write(filename="", text=""):
    """
    Method that appends content to the end of
    a text file and returns number of chars
    """
    with open(filename, "a", encoding='utf-8') as f:
        chars_num = f.write(text)
    return chars_num
