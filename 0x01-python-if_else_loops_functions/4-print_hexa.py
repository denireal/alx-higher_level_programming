#!/usr/bin/python3

"""
Author: Wari Denyefa
Description: This script prints decimal numbers from 0 to 98
along with their hexadecimal representations.
"""

# Iterate over numbers from 0 to 98
for number in range(99):
    # Print the decimal number and its hexadecimal representation
    print("{:d} = {}".format(number, hex(number)))
