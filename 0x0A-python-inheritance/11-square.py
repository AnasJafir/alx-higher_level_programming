#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
10-square module
"""


class Square(Rectangle):
    """class defines square and inhertis from Rectangle"""
    def __init__(self, size):
        """initialization of attributes"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """function to calculate area"""

        return self.__size ** 2

    def __str__(self):
        """function to return square description"""

        return "[Square] {}/{}".format(self.__size, self.__size)
