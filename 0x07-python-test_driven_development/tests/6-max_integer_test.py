#!/usr/bin/python3
"""
Unit tests for the max_integer function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Tests for the max_integer function.
    """

    def test_ordered(self):
        """
        Test max_integer with an ordered list.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered(self):
        """
        Test max_integer with an unordered list.
        """
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_at_beginning(self):
        """
        Test max_integer with a list where the maximum is at the beginning.
        """
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty(self):
        """
        Test max_integer with an empty list.
        """
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """
        Test max_integer with a list containing only one element.
        """
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """
        Test max_integer with a list of floating-point numbers.
        """
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)

    def test_ints_and_floats(self):
        """
        Test max_integer with a list containing both integers and floats.
        """
        self.assertEqual(max_integer([1.53, 15.5, -9, 15, 6]), 15.5)

    def test_string(self):
        """
        Test max_integer with a string.
        """
        self.assertEqual(max_integer("Denyefa"), 'r')

    def test_list_of_strings(self):
        """
        Test max_integer with a list of strings.
        """
        self.assertEqual(max_integer(["Denyefa", "is", "my", "name"]), "name")

    def test_empty_string(self):
        """
        Test max_integer with an empty string.
        """
        self.assertIsNone(max_integer(""))


if __name__ == '__main__':
    unittest.main()
