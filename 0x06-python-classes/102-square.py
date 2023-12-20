#!/usr/bin/python3

"""
This module defines the Square class, representing a square
with a specified size.
It includes methods for calculating the area and implementing various
comparison operators.
"""

class Square:
    """
    Defines the blueprint of a square.

    Attributes:
        size (int): An integer representing the object size.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """
        Gets the size private attribute value.

        Returns:
            int: The size private attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size private attribute value.

        Validates the assignment of the size private attribute.

        Args:
            value (int): The value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size**2

    def __eq__(self, o):
        """
        Defines the == comparison.

        Args:
            o (Square): The other square to compare.

        Returns:
            bool: True if sizes are equal, False otherwise.
        """
        return self.__size == o.__size

    def __ne__(self, o):
        """
        Defines the != comparison.

        Args:
            o (Square): The other square to compare.

        Returns:
            bool: True if sizes are not equal, False otherwise.
        """
        return self.__size != o.__size

    def __gt__(self, o):
        """
        Defines the > comparison.

        Args:
            o (Square): The other square to compare.

        Returns:
            bool: True if the size is greater, False otherwise.
        """
        return self.__size > o.__size

    def __ge__(self, o):
        """
        Defines the >= comparison.

        Args:
            o (Square): The other square to compare.

        Returns:
            bool: True if the size is greater or equal, False otherwise.
        """
        return self.__size >= o.__size

    def __lt__(self, o):
        """
        Defines the < comparison.

        Args:
            o (Square): The other square to compare.

        Returns:
            bool: True if the size is smaller, False otherwise.
        """
        return self.__size < o.__size

    def __le__(self, o):
        """
        Defines the <= comparison.

        Args:
            o (Square): The other square to compare.

        Returns:
            bool: True if the size is smaller or equal, False otherwise.
        """
        return self.__size <= o.__size
