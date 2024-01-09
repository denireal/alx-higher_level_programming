#!/usr/bin/python3

# Author: Denyefa Wari

def read_file(filename=""):
    """
    Read the content of a file and print it.

    :param filename: The name of the file to be read.
    """
    # Open the file in read mode ('r') with utf-8 encoding
    with open(filename, 'r', encoding="utf-8") as f:
        # Read the entire content of the file
        read_data = f.read()

        # Print the content without adding an extra newline at the end
        print(read_data, end='')
