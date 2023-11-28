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

    for letter in str:
        ascii_letter_code = ord(letter)

        # Check if the letter is lowercase
        if ascii_letter_code in range(97, 123):
            # Convert the letter to uppercase by subtracting 32 from the ASCII code
            ascii_letter_code = ascii_letter_code - 32

        # Print the uppercase letter
        print("{:c}".format(ascii_letter_code), end="")

    # Print a newline character after processing the entire string
    print()
