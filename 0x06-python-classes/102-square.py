#!/usr/bin/python3

"""
This script defines a Python class named Square.
Square represents a square with a specified size and includes comparison
operators based on the areas of two squares.
"""



class Square:
    def __init__(self, size=0):
        """
        Constructor method to initialize a Square.

        Parameters:
        - size (int): The size of the square (default is 0).
        """
        self.size = size

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
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Equality comparison based on the areas of two squares.

        Parameters:
        - other (Square): The other square to compare.

        Returns:
        bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparison based on the areas of two squares.

        Parameters:
        - other (Square): The other square to compare.

        Returns:
        bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparison based on the areas of two squares.

        Parameters:
        - other (Square): The other square to compare.

        Returns:
        bool: True if the area of self is less than the area of
		-other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to comparison based on the areas of two squares.

        Parameters:
        - other (Square): The other square to compare.

        Returns:
        bool: True if the area of self is less than or equal to the area
		- of other, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparison based on the areas of two squares.

        Parameters:
        - other (Square): The other square to compare.

        Returns:
        bool: True if the area of self is greater than the area of other,
		- False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal to comparison based on the areas of two squares.

        Parameters:
        - other (Square): The other square to compare.

        Returns:
        bool: True if the area of self is greater than or equal to the
		- area of other, False otherwise.
        """
        return self.area() >= other.area()
