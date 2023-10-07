#!/usr/bin/python3
"""Module containing a function that
prints a square
"""


def print_square(size):
    """function that prints a square with #
    size: The int size of the square's side
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
