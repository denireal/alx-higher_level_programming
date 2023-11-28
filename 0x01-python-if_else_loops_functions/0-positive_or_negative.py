#!/usr/bin/python3
"""
Author: Wari Denyefa
Description: This script generates a random number between -10 and 10
             and prints whether it is positive, negative, or zero.
"""

import random

# Generate a random number between -10 and 10 (inclusive)
number = random.randint(-10, 10)

# Check if the number is positive
if number > 0:
    print(f'{number} is positive')
# Check if the number is zero
elif number == 0:
    print(f'{number} is zero')
# If the number is not positive or zero, it must be negative
elif number < 0:
    print(f'{number} is negative')
