#!/usr/bin/python3

"""
Author: Wari Denyefa
Date: November 28, 2023

Description: This script prints the uppercase alphabet in
reverse order, excluding letters with even ASCII values.
"""

for lowercase_ascii in reversed(range(ord("a"), ord("z") + 1)):
    if lowercase_ascii % 2 != 0:
        uppercase_ascii = lowercase_ascii - 32
        uppercase_character = "{:c}".format(uppercase_ascii)
		print(uppercase_character, end="")
