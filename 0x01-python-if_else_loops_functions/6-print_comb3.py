#!/usr/bin/python3

"""
Author: Wari Denyefa
Description: This script generates and prints two-digit numbers
where the second digit is always greater than the first digit,
starting from 01 and ending with 89.
"""

# Iterate over possible first digits (0 to 7)
for first_digit in range(0, 8):
    # Iterate over possible second digits (0 to 9)
    for second_digit in range(0, 10):
        # Check if the second digit is greater than the first digit
        if not (second_digit <= first_digit):
            # Print the two-digit number
            print("{:d}{:d}".format(first_digit, second_digit), end=", ")

# Print the last number (89) without a trailing comma
print("89")
