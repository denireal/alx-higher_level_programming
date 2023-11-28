#!/usr/bin/python3

"""
Author: Wari Denyefa
Description: This script defines a function uppercase that takes a
character string as an argument and prints the uppercase version of
each lowercase letter in the string.
"""

def uppercase(str):
    """
    Prints the uppercase version of the input string followed by a new line.

    Args:
        str (str): The input string to be converted to uppercase.
    """
    result_str = ""

    for char in str:
        # Convert each character to uppercase without using str.upper()
        uppercase_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        result_str += uppercase_char

    # Print the final result followed by a new line
    print(result_str)
