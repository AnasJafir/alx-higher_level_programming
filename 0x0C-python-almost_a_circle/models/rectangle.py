#!/usr/bin/python3
"""Module for Base Class"""


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

    @property
    def height(self):
        """ retrieve height """
        return self.__height
    
    @property
    def x(self):
        """ retrieve x """
        return self.__x
    
    @property
    def y(self):
        """ retrieve y """
        return self.__y

    @width.setter
    def width(self, value):
        """ set width """
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height """
        self.__height = value
    
    @x.setter
    def height(self, value):
        """ set x """
        self.__x = value

    @y.setter
    def y(self, value):
        """ set y """
        self.__y = value
