#!/usr/bin/python3
"""Student Class Module"""


class Student():
    """Defining student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method that retrieves a
        dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        dct = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dct[key] = value
        return dct

    def reload_from_json(self, json):
        """Method that replaces all attributes of the Student instance"""
        json = self.__dict__
