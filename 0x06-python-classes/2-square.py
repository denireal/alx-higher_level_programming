#!/usr/bin/python3

"""
This script defines a Python class named Square with a constructor
to initialize the size of a square.

Usage Example:

    Square = __import__('2-square').Square

    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

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
