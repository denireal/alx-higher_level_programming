#!/usr/bin/python3
"""
2-args.py - Program to print command line arguments.

This program prints the number of command line arguments and their values.

"""


from sys import argv

# Calculate the number of command line arguments
num_arguments  = len(argv) - 1

if __name__ == "__main__":
    # Print appropriate message based on the number of arguments
    if argv_length != 1:
        print("{:d} arguments:".format(num_arguments ))
    else:
        print("{:d} argument:".format(num_arguments ))

    # Iterate over command line arguments and print their index and value
    for arg_index, arg_value in enumerate(argv[1:], start=1):
        print("{:d}: {}".format(arg_index, arg_value))
