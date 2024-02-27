#!/usr/bin/python3
"""Rectangle Class Module"""
from models.base import Base


class Rectangle(Base):
    """Defining Rectangle Class that inherits from Base Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)  # Calling the parent class constructor

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, (int, float)):
            self.__width = value
        else:
            raise ValueError("Width must be a number")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError('Height must be an integer')

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
