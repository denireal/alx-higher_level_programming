#!/usr/bin/python3
"""
3-infinite_add.py - Program to add command line arguments.

This program adds all command line arguments and prints the result.

"""


from sys import argv

if __name__ == "__main__":
    # Ensure there are more than one arguments (script name is also an argument)
    if len(argv) > 1:
        # Use the sum() function to add all integer arguments
        result = sum(int(arg) for arg in argv[1:])
        print(result)
    else:
        print("No arguments provided.")
