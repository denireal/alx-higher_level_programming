#!/usr/bin/python3

"""
This script defines a Python class named Square with a property
to get and set the size, and a method to calculate the area of a square.
"""


class Square:
    def __init__(self, size=0):
        """
        Constructor method to initialize the size of the square.

        Parameters:
        - size (int): The size of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """
        Property to get the size of the square.

        Returns:
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter to set the size of the square.

        Parameters:
        - value (int): The new size of the square.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square.
        """
        return (self.__size ** 2)
