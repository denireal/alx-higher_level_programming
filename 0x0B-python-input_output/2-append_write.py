#!/usr/bin/python3

"""
Function that appends to a text file.
"""


def append_write(filename, text):
    """
    Function that appends to a text file.

    Args:
        filename (str): The name of the file to be appended.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters appended to the file.
    """
    # Open the file in append mode ('a') with utf-8 encoding
    with open(filename, 'a', encoding="utf-8") as f:
        # Append the text to the file
        return f.write(text)
