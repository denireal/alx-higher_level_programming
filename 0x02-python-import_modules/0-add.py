#!/usr/bin/python3
"""
0-add.py - Program to demonstrate importing and using a function.

Description: This program imports the add function from add_0.py, assigns values
to variables a and b, calls the add function, and prints the result
in a formatted string.

"""


if __name__ == "__main__"
    # Importing the add function from add_0.py module
    from add_0 import add

    # Assigning values to variables a and b
    a = 1
    b = 2

    # Calling add func and printing result in a formatted string
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
