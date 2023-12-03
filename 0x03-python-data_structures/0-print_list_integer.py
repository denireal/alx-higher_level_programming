#!/usr/bin/python3
"""
print_list_integer.py - Program to print each integer in a list.

This program defines a function 'print_list_integer' that takes a
list of integers as a parameter and prints each integer in the list.

"""


def print_list_integer(my_list=[]):
    """
    Print each integer in the given list.

    Args:
        my_list (list): List of integers to be printed.
    """
    for n in my_list:
        # Print each integer using format
        print("{:d}".format(n))
