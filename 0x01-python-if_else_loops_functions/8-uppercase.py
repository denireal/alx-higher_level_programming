#!/usr/bin/python3

"""
Author: Wari Denyefa
Description: This script defines a function uppercase that takes a
character string as an argument and prints the uppercase version of
each lowercase letter in the string.
"""

def uppercase(input_str):
    """
    Prints the uppercase version of the input string followed by a new line.

    Args:
        input_str (str): The input string to be converted to uppercase.
    """
    result_str = ""

    for char in input_str:
        # Convert each character to uppercase without using str.upper()
        result_str += chr(ord(char) - 32) if 'a' <= char <= 'z' else char

    print("{:s}".format(result_str))
