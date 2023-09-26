#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represent a square
    Attributes:
        __size (int): length of a side of the square
    """
    def __init__(self, size=0):
        """initialization of the square
        Args:
            size (int): length of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates the area of the square
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """get __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
