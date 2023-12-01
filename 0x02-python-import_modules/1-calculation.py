#!/usr/bin/python3
"""
1-calculation.py - Main script to demonstrate calculator functions.

This script imports add, sub, mul, and div functions from the calculator_1 module
and performs arithmetic operations.

"""

# Importing functions from calculator_1 module
from calculator_1 import add, sub, mul, div

# Assigning values to variables a and b
a = 10
b = 5

# Main block to ensure the code is only executed when this script is run, not w
if __name__ == "__main__":
	# Performing addition and printing the result
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

    # Performing subtraction and printing the result
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))

    # Performing multiplication and printing the result
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))

    # Performing division and printing the result
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
