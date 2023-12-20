#!/usr/bin/python3

"""
This module defines the MagicClass, which represents a geometric shape with
a specified radius.
It provides methods for calculating the area and circumference of the shape.
"""



import math

class MagicClass:
    """
    MagicClass models a geometric shape with a defined radius.
    It includes methods for computing the area and circumference.
    """

    def __init__(self, radius=0):
        """
        Constructor method for initializing a MagicClass instance.

        Parameters:
        - radius (int or float): Radius of the geometric shape (default is 0)
        """
        self.__radius = 0
        if type(radius) not in {int, float}:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Compute and return the area of the geometric shape.

        Returns:
        float: The area of the geometric shape.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Compute and return the circumference of the geometric shape.

        Returns:
        float: The circumference of the geometric shape.
        """
        return 2 * math.pi * self.__radius

# Example usage:
# my_magic = MagicClass(radius=5)
# print(my_magic.area())
# print(my_magic.circumference())
