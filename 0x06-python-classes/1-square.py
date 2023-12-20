#!/usr/bin/python3

"""Square Module.

This module defines a Python class named Square.

Usage Example:

    from 1-square import Square

    # Create an instance of the Square class with size 3
    my_square = Square(3)

    # Print the type and dictionary representation of the instance
    print(type(my_square))
    print(my_square.__dict__)
"""

class Square:
    """Defines the blueprint of a square.

    Attribute:
        size (int): An integer indicating the size of the square object.
    """

    def __init__(self, size):
        """An object constructor method.

        Initializes Square with a given size.

        Args:
            size (int): An integer representing the object size.
        """
        self.__size = size
