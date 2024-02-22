#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Class that defines properties of rectangle"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width retriver"""
        return self.__width

    @property
    def height(self):
        """Height retriver"""
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height of recyangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method that returns the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Method that return the perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2*(self.width + self.height)

    def __str__(self):
        """Presentation of the rectangle with char #"""
        string = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                string.append("#")
            string.append("\n")
        string.pop()
        return "".join(string)

    def __repr__(self):
        """Method that returns a string representation of the rectangle"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Method to print an expression after instance deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
