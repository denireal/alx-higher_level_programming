#!/usr/bin/python3

"""
Author: Wari Denyefa
Description: This script defines a function fizzbuzz that prints
the FizzBuzz sequence up to 100.
"""

def fizzbuzz():
    """Prints the FizzBuzz sequence up to 100"""
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz', end=' ')
        elif i % 5 == 0:
            print('Buzz', end=' ')
        elif i % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{}".format(i), end=' ')
