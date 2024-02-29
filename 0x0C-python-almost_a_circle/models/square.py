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

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute"""
        if args is not None and len(args) != 0:
            kwargs = {}
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        for key, value in kwargs.items():
            if key == "id":
                if type(value) != int and value is not None:
                    raise TypeError("id must be an integer")
                self.id = value
            if key == "size":
                self.__width = value
            if key == "x":
                self.__x = value
            if key == "y":
                self.__y = value
