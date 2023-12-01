#!/usr/bin/python3
"""
5-variable_load.py - Program to import and print a variable.

This program imports the variable 'a' from the variable_load_5 module
and prints its value.

"""


if __name__ == "__main__":
    # Importing variable 'a' from variable_load_5 module
    from variable_load_5 import a

    # Printing the value of variable 'a'
    print("{:d}".format(a))
