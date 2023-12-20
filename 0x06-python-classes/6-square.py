#!/usr/bin/python3

"""Square Class.

This module contains a class that defines a square.

Usage Example:

    Square = __import__('6-square').Square

    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
"""


class Square:
    '''Defines the blueprint of a square.

    Attributes:
        size (int): An integer indicating the size of the square object.
        position (tuple): A tuple of two positive integers representing
                          the position of the square.
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''Object constructor method.

        Initializes Square with a given size and position.

        Args:
            size (int): An integer representing the object size.
                Defaults to 0.
            position (tuple): A tuple of two positive integers representing
                              the position of the square.
                Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple
                       of two positive integers.
            ValueError: If size is less than 0 or position contains negative
                         integers.
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Retrieves the size of the square.'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Sets the size of the square.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''Retrieves the position of the square.'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Sets the position of the square.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If position is not a tuple or does not contain two
                       integers.
            ValueError: If position contains negative integers.
        '''
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Calculates and returns the area of the square.'''
        return self.__size ** 2

    def my_print(self):
        '''Prints the square using '#' character.'''
        if self.__size == 0:
            print("")
            return
        [print("") for _ in range(0, self.__position[1])]

        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(0, self.__size)]
            print("")
