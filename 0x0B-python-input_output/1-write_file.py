#!/usr/bin/python3

"""
Write the given text to a file.
"""

def write_file(filename="", text=""):
    """
    Write the given text to a file.

    Args:
        filename: The name of the file to be written.
        text: The text to be written to the file.
    
    return: The number of characters written to the file.
    """
    # Open the file in write mode ('w') with utf-8 encoding
    with open(filename, 'w', encoding="utf-8") as f:
        # Write the text to the file
        return f.write(text)
