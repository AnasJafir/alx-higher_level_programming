#!/usr/bin/python3
""" Definition of a square class """
class Square:
    """ Defines a square
    Attributes:
    __size (int): length of one side of the square
    __position (tuple): position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialization of the square
        Args:
        size (int): length of one side of the square
        position (tuple): position of the square
        Returns: None
        """
        self.size = size
        self.position = position

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
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for a in range(self.__position[0])]), end="")
            print("".join(["#" for b in range(self.__size)]))
    @property
    def position(self):
        """get the postion of the square
        Returns: The position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position
        Args:
            value (tuple): position of the square in 2D space
        Returns: None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
