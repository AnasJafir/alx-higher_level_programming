#!/usr/bin/python3
"""Module for Rectangle Class"""


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """ retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        self.__width = value

    @property
    def height(self):
        """ retrieve height """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ set height """
        self.__height = value

    @property
    def x(self):
        """ retrieve x """
        return self.__x
    
    @x.setter
    def height(self, value):
        """ set x """
        self.__x = value
    
    @property
    def y(self):
        """ retrieve y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y """
        self.__y = value
