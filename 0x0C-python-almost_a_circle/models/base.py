#!/usr/bin/python3
"""Base Class module"""
import json


class Base:
    """Defining Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of Base class"""
        if id is not None:
            self.id = id
        else:
            # After each creation of an instance of Base class
            # a new id number should be assigned
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method that returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method that writes the JSON string representation
        of list_objs to a file
        """
        if list_objs is None or list_objs == []:
            json_str = "[]"
        else:
            json_str = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
                )
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the JSON string representation"""
        lst = []
        if json_string is None or json_string == [{""}]:
            return []
        lst = json.loads(json_string)
        return lst
