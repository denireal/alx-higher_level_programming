#!/usr/bin/python3

"""
This script defines a Python class named Square with methods
to initialize the size and calculate the area of a square.
"""

class Square:
    def __init__(self, size=0):
        """
        Constructor method to initialize the size of the square.

        Parameters:
        - size (int): The size of the square (default is 0).

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size
