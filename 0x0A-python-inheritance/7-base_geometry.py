#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """Class that represents the base geometry class."""
    def area(self):
        """Calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
