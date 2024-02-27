#!/usr/bin/python3
"""Square class Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of class"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the size attribute."""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size attribute."""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
            )
