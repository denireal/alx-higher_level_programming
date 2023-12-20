#!/usr/bin/python3
"""Square Module.

This module defines a Python class named Square.

Usage Example:

    from 2-square import Square

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

    def __init__(self, size=0):
        """An object constructor method.

        Initializes Square with a given size.

        Args:
            size (int): An integer representing the object size.
                Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
