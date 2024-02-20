#!/usr/bin/python3
"""Square module"""


def print_square(size):
    """Method that prints a square with a given size"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
