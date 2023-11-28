#!/usr/bin/python3

"""
Author: Wari Denyefa
Description: This script prints all lowercase letters from 'a' to 'z'
             excluding 'e' and 'q' using their corresponding ASCII codes.
"""

# Iterate over ASCII codes for lowercase letters (97 to 122)
for ascii_code in range(97, 123):

    # Skip printing for 'e' (ASCII code 101) and 'q' (ASCII code 113)
    if ascii_code == 101 or ascii_code == 113:
        continue

    # Print the character corresponding to the current ASCII code
	print("{:c}".format(ascii_code), end='')
