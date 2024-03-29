#!/usr/bin/python3
"""
Unit tests for the max_integer function
"""

import unittest
from typing import List, Union

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class containing unit tests for the max_integer function
    """

    def test_ordered_list(self):
        """
        Test max_integer function with an ordered list
        """
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """
        Test max_integer function with an unordered list
        """
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """
        Test max_integer function with the maximum at the beginning of the list
        """
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """
        Test max_integer function with an empty list
        """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """
        Test max_integer function with a list containing only one element
        """
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """
        Test max_integer function with a list of floats
        """
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """
        Test max_integer function with a list containing both
        integers and floats
        """
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """
        Test max_integer function with a string
        """
        string = "Denyefa"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """
        Test max_integer function with a list of strings
        """
        strings = ["Denyefa", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """
        Test max_integer function with an empty string
        """
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
