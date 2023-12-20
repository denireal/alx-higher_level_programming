#!/usr/bin/python3

"""
This script defines a Python class named MagicClass.
MagicClass represents a geometric shape with a radius and includes
methods for calculating the area and circumference.
"""


import math

class MagicClass:
    def __init__(self, radius=0):
        """
        Constructor method to initialize a MagicClass.

        Parameters:
        - radius (int or float): The radius of the geometric shape
		- (default is 0).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the geometric shape.

        Returns:
        float: The area of the geometric shape.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate and return the circumference of the geometric shape.

        Returns:
        float: The circumference of the geometric shape.
        """
        return 2 * math.pi * self.__radius
