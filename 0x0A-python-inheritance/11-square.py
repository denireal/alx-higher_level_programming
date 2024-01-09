#!/usr/bin/python3
"""
Module defining a Square class based on Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.

    Attributes:
        __size (int): Size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Gets a string representation of the Square.

        Returns:
            str: A string representating "[Square] {size}/{size}".
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
