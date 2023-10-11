#!/usr/bin/python3
"""
5-base_geometry module
"""


class BaseGeometry:
    """basegeometry class"""

    @classmethod
    def area(self):
        """ area - defines area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function to check if value is a positive int """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
