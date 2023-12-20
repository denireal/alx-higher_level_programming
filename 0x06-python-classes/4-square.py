#!/usr/bin/python3
"""Square Module.

This module defines a Python class named Square.

Usage Example:

    from <module_name> import Square

    # Create an instance of the Square class with a specified size
    my_square = Square(size)

    # Get and print the area of the square
    print(my_square.area())
"""

class Square:
    """Defines the blueprint of a square.

    Attributes:
        size (int): An integer indicating the size of the square object.
    """

    def __init__(self, size=0):
        """Object constructor method.

        Initializes Square with a given size.

        Args:
            size (int): An integer representing the object size.
                Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
