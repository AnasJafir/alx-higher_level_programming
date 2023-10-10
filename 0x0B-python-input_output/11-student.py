#!/usr/bin/python3
"""
9-student module
"""


class Student:
    """
        Class students that defines student
        Attributes:
            first_name: first name of student.
            last_name: last name of student.
            age: age of student.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialization of Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self, attrs=None):
        """
        Method to retrieve a dictionary representation of a Student
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict 
    def reload_from_json(self, json):
        '''replaces all attributes of the Student'''
        for key, value in json.items():
            self.__dict__[key] = value
