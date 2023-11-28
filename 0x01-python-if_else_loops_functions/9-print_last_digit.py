#!/usr/bin/python3

"""
Author: Wari Denyefa
Description: This script defines a function print_last_digit that takes
a number as an argument, prints the last digit of that number, and returns
the value of the last digit.
"""

def print_last_digit(number):
    """Prints the last digit of the input number

    Args:
        number: a number

    Returns:
        last_digit: the value of the last digit
    """

    # Get the last digit using the modulo operator
    last_digit = number % 10

    # Print the last digit
    print(last_digit, end="")

    # Return the value of the last digit
    return last_digit
