#!/usr/bin/python3
"""
Author: Wari Denyefa
Description: This script generates a random number between -10000 and 10000,
             extracts its last digit, and prints information based on the
             properties of the last digit.
"""

import random

# Generate a random number between -10000 and 10000 (inclusive)
number = random.randint(-10000, 10000)

# Get and store the last digit of the number in a variable named last_digit
last_digit = int(repr(number)[-1])

# Check if the last digit is greater than 5
if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit))

# Check if the last digit is less than 6 and not 0
elif last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))

# Check if the last digit is 0
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
