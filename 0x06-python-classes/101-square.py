#!/usr/bin/python3

"""
This script defines a Python class named Square.
Square represents a square with a specified size and position.
"""



class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor method to initialize a Square.

        Parameters:
        - size (int): The size of the square (default is 0).
        - position (tuple): The position of the square in a two-dimensional
		- space (default is (0, 0)).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Property to get the position of the square.

        Returns:
        tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Property setter to set the position of the square.

        Parameters:
        - value (tuple): The new position of the square.

        Raises:
        - TypeError: If the value is not a tuple of 2 integers.
        - ValueError: If any value in the tuple is less than 0.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
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

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        str: String representation of the square.
        """
        if self.__size != 0:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.__size):
                    print("#", end="")
                if _ != self.__size - 1:
                    print("")
        return ""
