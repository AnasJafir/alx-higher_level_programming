#!/usr/bin/python3
"""BaseGeometry module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class that inherits  from Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
