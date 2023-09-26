#!/usr/bin/python3
""" Definition of a square class """


class Square:
    """ Defines a square
    Attributes:
    _size (int): length of one side of the square
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
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """ print square
        Returns: None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
