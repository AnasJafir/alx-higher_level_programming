#!/usr/bin/python3
"""Rectangle Class Module"""


class Rectangle():
    """class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation Method"""
        if type(width) != int or type(height) != int:
            raise TypeError("width must be an integer")
        elif width <= 0 or height <= 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Method to retrieve value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method  to set the value of width with validation"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Method to retrieve value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set the value of height with validation"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
