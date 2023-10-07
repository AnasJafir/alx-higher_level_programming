#!/usr/bin/python3
"""Unittest for the function
max_integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases
    """

    def test_max_integer_in_end(self):
        """Test max_integer of a list at the end
        """
        lst = [1, 2, 3, 4]
        self.assertEqual(max_integer(lst), 4)

    def test_max_integer_in_first(self):
        """Test max_integer of a list at the beginning
        """
        lst = [4, 1, 2, 3]
        self.assertEqual(max_integer(lst), 4)

    def test_max_integer_in_middle(self):
        """Test max_integer in the middle of a list
        """
        lst = [1, 4, 2, 3]
        self.assertEqual(max_integer(lst), 4)

    def test_max_negative_integer(self):
        """Checks the max_negative_integer of a list
        """
        lst = [-1, -2, -3, -4]
        self.assertEqual(max_integer(lst), -1)

    def test_float(self):
        """Checks the max_float of a list
        """
        lst = [1, 2, 3.3, 4.5]
        self.assertEqual(max_integer(lst), 4.5)

    def test_string(self):
        """Checks max_integer with a string in list
        """
        lst = [1, 2, '3', 4]
        with self.assertRaises(TypeError):
            max_integer(lst)

    def test_list_one_element(self):
        """ Checks the case of one element in list
        """
        lst = [2]
        self.assertEqual(max_integer(lst), 2)

    def test_empty_list(self):
        """Checks the case of an empty list
        """
        lst = []
        self.assertEqual(max_integer(lst), None)

    def test_void_arg(self):
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
