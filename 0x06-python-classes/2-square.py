#!/usr/bin/python3
""" Definition of a square class """


class Square:
    """ Defines a square
    Attributes:
        __size (int): length of one side of the square
    """
    def __init__(self, size=0):
        """initialization of the square
        Args:
            size (int): length of one side of the square
        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
