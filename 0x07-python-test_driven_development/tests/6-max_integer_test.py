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

    def test_negatives(self):
        """Check if it raises an exception when given negative numbers."""
        self.assertEqual(max_integer([-5, -4, -3]), -3)

    def test_zero(self):
        """Check if it handles zero correctly."""
        self.assertEqual(max_integer([0, 10, 20]), 20)


if __name__ == "__main__":
    unittest.main()
