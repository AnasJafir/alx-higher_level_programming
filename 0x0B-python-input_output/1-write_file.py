#!/usr/bin/python3
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    write_file - write a text into a file
    Args:
        filename: the name of file
        text: text to write in the file
    Return: the number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return (f.write(text))
