#!/usr/bin/python3
""" Definition of a square class """


class Square:
    """ Defines a square
    Attributes:
        __size (int): length of one side of the square
    """
    def __init__(self, size):
        """initialization of the square
        Args:
            size (int): length of one side of the square
        Returns: None
        """
        self.__size = size
