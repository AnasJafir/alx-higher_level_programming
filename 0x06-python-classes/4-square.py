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
        self.size = size

    def area(self):
        """ Defines the current square area
        Returns: 
        the current square area
        """
        return self.__size ** 2
    @property
    def size(self):
        """to retrieve the size of the square
        Returns: the size of the square
        """
        return self.__size
    @size.setter
    def size(self, value):
        """set the size
        Args:
        value (int): the size of the square
        Returns: None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else :
                self.__size = value
