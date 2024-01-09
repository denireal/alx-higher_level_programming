#!/usr/bin/python3
"""
Creates a Square class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a square.

    Attributes:
        __size (int): Size of the square.
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Get a string representation of the Square.

        Returns:
            str: A string representating "[Square] {size}/{size}".
        """
        return super().__str__()

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
