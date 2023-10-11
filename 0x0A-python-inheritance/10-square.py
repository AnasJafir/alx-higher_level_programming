#!/usr/bin/python3
"""
10-square module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class defines square and inhertis from Rectangle"""
    def __init__(self, size):
        """initialization of attributes"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """function to calculate area"""
        return self.__size ** 2
