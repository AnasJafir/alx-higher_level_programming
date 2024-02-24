#!/usr/bin/python3
"""
Module of class that prevents the user from
dynamically creating new instance attributes
except if the new instance attribute is called first_name
"""


class LockedClass:
    """
    A class that prevents the user from
    dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """
    def __setattr__(self, attr, value):
        if attr != "first_name":
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(attr)
                )
        self.__dict__[attr] = value
