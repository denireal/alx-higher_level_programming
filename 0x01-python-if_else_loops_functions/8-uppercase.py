#!/usr/bin/python3

"""
Author: Wari Denyefa
Description: This script defines a function uppercase that takes a
character string as an argument and prints the uppercase version of
each lowercase letter in the string.
"""

def _upper(char):
    """
    Converts a lowercase character to uppercase.

    Args:
        char (str): The input character.

    Returns:
        int: The ASCII code of the uppercase character.
    """
    if 'a' <= char <= 'z':
        return ord(char) - 32
    else:
        return ord(char)


def uppercase(input_str):
    """
    Prints the uppercase version of the input string followed by a new line.

    Args:
        input_str (str): The input string to be converted to uppercase.
    """
    result_str = ""

    for char in input_str:
        # Convert each character to uppercase without using str.upper()
        result_str += "%c" % _upper(char)
    print(result_str)
