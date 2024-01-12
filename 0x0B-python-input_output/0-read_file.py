#!/usr/bin/python3

# Author: Denyefa Wari


def read_file(filename=""):
    """
    Read the content of a file and print it.

    filename: The name of the file to be read.
    """
    # Open the file in read mode ('r') with utf-8 encoding
    with open(filename, encoding="utf-8") as f:
        # Print the content without adding an extra newline at the end
        print(f.read() end='')
