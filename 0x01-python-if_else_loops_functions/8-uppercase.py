#!/usr/bin/python3

"""
Author: Wari Denyefa
Description: This script defines a function uppercase that takes a
character string as an argument and prints the uppercase version of
each lowercase letter in the string.
"""

def uppercase(str):
    """Prints uppercase string

    Args:
        str: a character string argument
    """

    # For each character in input_str
    for char in str:

        # Get the character's ASCII code
        ascii_char_code = ord(char)

        # If the character is in the lowercase range
        if 97 <= ascii_char_code <= 122:

            # Convert it to the uppercase value
            ascii_char_code -= 32

        # Print out the uppercase value as a character
        print("{:c}".format(ascii_char_code), end="")
    print()
