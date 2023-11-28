#!/usr/bin/python3

"""
Author: Wari Denyefa
Description: This script defines a function uppercase that takes a
character string as an argument and prints the uppercase version of
each lowercase letter in the string.
"""

def _upper(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return (ord(char) - 32)
    else:
        return ord(char)

def uppercase(str):
    """
    Prints the uppercase version of the input string followed by a new line.

    Args:
        str (str): The input string to be converted to uppercase.
    """
    result_str = ""

    for char in str:
        # Convert each character to uppercase without using str.upper()
        result_str += "%c" % _upper(char)
        print("{:s}".format(result_str))
