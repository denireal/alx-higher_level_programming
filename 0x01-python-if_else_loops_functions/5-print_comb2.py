#!/usr/bin/python3

"""
Author: Wari Denyefa
Description: This script prints numbers from 0 to 99
as two-digit numbers separated by commas.
"""

# Iterate over numbers from 0 to 98
for number in range(0, 99):
    # Print the two-digit formatted number followed by a comma and space
	print("{:02d}".format(number), end=", ")

# Print the last number (99) without a trailing comma
print(99)
