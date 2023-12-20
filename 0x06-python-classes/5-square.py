#!/usr/bin/python3


"""Square Class.

This module contains a class that defines a square.

Usage Example:

    Square = __import__('5-square').Square

    my_square = Square(5)
    print(type(my_square))
    print(my_square.__dict__)
"""

class Square:
    '''Defines the blueprint of a square.

    Attributes:
        size (int): An integer indicating the size of the square object.
    '''

    def __init__(self, size=0):
        '''Object constructor method.

        Initializes Square with a given size.

        Args:
            size (int): An integer representing the object size.
                Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        self.size = size

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

    def area(self):
        '''Calculates and returns the area of the square.'''
        return self.__size ** 2

    def my_print(self):
        '''Prints the square using '#' character.'''
        for _ in range(0, self.__size):
            [print("#", end="") for _ in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
