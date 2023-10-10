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

    def to_json(self):
        """
        Method to retrieve a dictionary representation of a Student
        """
        return self.__dict__
