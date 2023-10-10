#!/usr/bin/python3
"""
2-append_write module
"""


def append_write(filename="", text=""):
    """
    append_file - append a text to a file
    Args:
        filename: the name of file
        text: text to append to the file
    Return: the number of characters written
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return (f.write(text))
