#!/usr/bin/python3
"""Base Class module"""


class Base:
    """Defining Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
