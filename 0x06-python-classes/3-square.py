#!/usr/bin/python3

"""
This script defines a Python class named Square with methods
to initialize the size and calculate the area of a square.


Usage Example:

    from <module_name> import Square

    # Create an instance of the Square class with a specified size
    my_square = Square(size)

    # Calculate and print the area of the square
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
