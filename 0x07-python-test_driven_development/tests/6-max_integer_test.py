#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestStringMethods(unittest.TestCase):
    """Class to test 'max_integer' function"""

    def test_positives(self):
        """Check if it returns the maximum of a list with positive integers."""
        self.assertEqual(max_integer([1, 2, 3]),  3)
        self.assertEqual(max_integer([10, 20, 30]), 30)

    def test_max_at_the_beginning(self):
        """Check if it returns the maximum that is in the beginning of a list"""
        self.assertEqual(max_integer([10, -10, 7]), 10)

    def test_max_at_the_middle(self):
        """Check if it can find the maximum number when it's not at the beginning or end"""
        self.assertEqual(max_integer([-5, 8, -12]), 8)

    def test_one_elm(self):
        """Check if it returns the max integer of a list of one integer"""
        self.assertEqual(max_integer([9]), 9)

    def test_negatives(self):
        """Check if it raises an exception when given negative numbers."""
        self.assertEqual(max_integer([-5, -4, -3]), -3)

    def test_zero(self):
        """Check if it handles zero correctly."""
        self.assertEqual(max_integer([0, 10, 20]), 20)


if __name__ == "__main__":
    unittest.main()
