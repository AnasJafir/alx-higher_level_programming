#!/usr/bin/python3
"""Module containing a function that prints indentation"""


def text_indentation(text):
    """function that adds 2 new lines after '.?:' chars.
    text: The str text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiters in ".?:":
        text = (delimiters + "\n\n").join(
            [line.strip(" ") for line in text.split(delimiters)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
