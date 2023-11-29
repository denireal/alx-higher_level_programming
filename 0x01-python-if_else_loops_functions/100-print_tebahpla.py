#!/usr/bin/python3


"""
Author: Wari Denyefa
Date: November 28, 2023

Description: This script prints the uppercase alphabet in
reverse order, excluding letters with even ASCII values.
"""


for ascii_digit in range (122, 96, -1):


    if ascii_digit % 2 == 1:

        ascii_digit = ascii_digit - 32

        print("{:c}".format(ascii_digit), end="")
