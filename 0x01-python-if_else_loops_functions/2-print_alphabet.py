#!/usr/bin/python3
"""
Author: Wari Denyefa
Description: This script prints all lowercase letters from 'a' to 'z'
             using their corresponding ASCII codes.
"""

current_ascii = ord('a')

while current_ascii <= ord('z'):
    print("{:s}".format(chr(current_ascii)), end="")
    current_ascii += 1

print()  # Add a newline after printing the alphabet
