#!/usr/bin/python3
"""
Module of class that prevents the user from
dynamically creating new instance attributes
except if the new instance attribute is called first_name
"""


class LockedClass:
    """A class to prevent adding new attributes except for 'first_name'."""
    def __setattr__(self, attr, value):
        """
        Checks whether an attempt to add a new attribute is made.
        If so, it raises an exception.
        """
        if attr != "first_name":
            raise AttributeError(
                f"'LockedClass' object has no attribute '{attr}'"
                )
        else:
            super().__setattr__(attr, value)

    def __getattribute__(self, attr):
        """
            Override the reserved method `getattr` to preven retrieval of any
            attributes, including instance's dict.

            Args:
                name (:obj:`str`): A string.
        """
        if attr == "__dict__":
            raise AttributeError(
                f"'LockedClass' object has no attribute '{attr}'"
                )
