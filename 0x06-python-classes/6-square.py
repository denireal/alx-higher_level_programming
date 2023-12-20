#!/usr/bin/python3

"""
This script defines a Python class named Square with properties to get and set
the size, position, methods to calculate the area, and print a representation
of the square.
"""

class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor method to initialize the size and position of the square.

        Parameters:
        - size (int): The size of the square (default is 0).
        - position (tuple): Position of the square in a two-dimensional space
		- (default is (0, 0)).
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Property to get the size of the square.

        Returns:
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, new_size):
        """
        Property setter to set the size of the square.

        Parameters:
        - new_size (int): The new size of the square.

        Raises:
        - TypeError: If new_size is not an integer.
        - ValueError: If new_size is less than 0.
        """
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    @property
    def position(self):
        """
        Property to get the position of the square.

        Returns:
        tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, new_position):
        """
        Property setter to set the position of the square.

        Parameters:
        - new_position (tuple): The new position of the square.

        Raises:
        - TypeError: If new_position is not a tuple of 2 integers.
        - ValueError: If any value in new_position is less than 0.
        """
        if (
            not isinstance(new_position, tuple)
            or len(new_position) != 2
            or not all(isinstance(coord, int) for coord in new_position)
            or not all(coord >= 0 for coord in new_position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = new_position

    def calculate_area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2

    def display_square(self):
        """
        Print a representation of the square, considering the position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.__size):
                print("#", end="")
            print("")
