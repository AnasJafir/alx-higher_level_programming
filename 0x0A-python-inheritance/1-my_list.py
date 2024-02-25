#!/usr/bin/python3
"""myList Module"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """
        Method that prints the list
        but sorted (ascending sort)
        """
        sorted_list = sorted(self)
        print(sorted_list)
