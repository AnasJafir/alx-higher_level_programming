#!/usr/bin/python3
"""Module of indentation"""


def text_indentation(text):
    """Method prints a new line after specific chars"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    skip_spaces = False

    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            print(text[i])
            skip_spaces = True
        elif text[i] == ' ' and skip_spaces:
            continue
        else:
            print(text[i], end='')
            skip_spaces = False
