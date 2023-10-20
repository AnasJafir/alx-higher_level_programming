#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        self.__width = value

    @property
    def height(self):
        """Height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        self.__height = value

    @property
    def x(self):
        """x of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        self.__x = value

    @property
    def y(self):
        """y of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        self.__y = value
