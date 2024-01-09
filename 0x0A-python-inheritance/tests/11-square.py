#!/usr/bin/python3
"""
Create a Square class based on Rectangle.
"""


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
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Get a string representation of the Square.

        Returns:
            str: A string representating "[Square] {size}/{size}".
        """
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__size, self.__size))
