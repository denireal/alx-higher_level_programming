#!/usr/bin/python3
"""
Author: Wari Denyefa
Description: This script generates a random number between -10000 and 10000,
             extracts its last digit, and prints information based on the
             properties of the last digit.
"""

import random

number = random.randint(-10000, 10000)

last_digit = int(repr(number)[-1])

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")

elif 0 < last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")

elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
