#!/usr/bin/python3
"""BaseGeometry module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class that inherits  from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
