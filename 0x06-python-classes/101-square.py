#!/usr/bin/python3


"""Square Class.

This module contains a class that represents a square.

Usage Example:

    from 101-square import Square

"""



class Square:
    """Defines a square with a specified size and position.

    Attributes:
        size (int): An integer representing the size of the square.
        position (int, int): A tuple representing the position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square object with the given size and position."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square.

        Returns:
            tuple: A tuple representing the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): A tuple representing the new position.

        Raises:
            TypeError: If the value is not a tuple of two integers.
            ValueError: If the values in the tuple are less than 0.
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
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """Prints the square using '#' characters."""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(0, self.__size)]
            print("")

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: A string representing the square.
        """
        if self.__size != 0:
            [print("") for _ in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(0, self.__size)]
            if _ != self.__size - 1:
                print("")
        return ""
