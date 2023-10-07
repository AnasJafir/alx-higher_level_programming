#!/usr/bin/python3
"""Module containing a function to
say my name
"""


def say_my_name(first_name, last_name=""):
    """function that prints first and last name.
    first_name: first name string.
    last_name: last name string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
