#!/usr/bin/python3
"""
1-my_list module
"""


class MyList(list):
    """Class that defines MyList"""
    def print_sorted(self):
        """
        print_sorted - prints sorted list
        """
        print(sorted(list(self)))
