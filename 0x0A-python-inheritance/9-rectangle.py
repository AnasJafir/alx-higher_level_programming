#!/usr/bin/python3
"""
8-rectangle module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that defines a rectangle"""
    def __init__(self, width, height):
        """initialization of attributes"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """function to redefine area in parent class"""
        return self.__width * self.__height

    def __str__(self):
        """function to return object description"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
