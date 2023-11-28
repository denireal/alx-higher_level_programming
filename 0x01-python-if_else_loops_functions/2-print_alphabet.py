#!/usr/bin/python3
"""
Author: Wari Denyefa
Description: This script prints all lowercase letters from 'a' to 'z'
             using their corresponding ASCII codes.
"""

# Iterate over ASCII codes for lowercase letters (97 to 122)
for ascii_code in range(97, 123):
    # Print the character corresponding to the current ASCII code
	print("{:c}".format(ascii_code), end='')
