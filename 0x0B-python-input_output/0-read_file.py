#!/usr/bin/python3
"""
Read content from a file.
"""


def read_file(filename=""):
    """
    Read content from a file.

    Args:
        filename (str): The name of the file to be read.

    Raises:
        Exception: For any unexpected errors during file reading.
    """

    try:
        with open(filename, 'r', encoding="utf-8") as file:
            read_data = file.read()
            print(read_data, end='')
    except Exception as e:
        raise Exception(
                f"Error: An error occurred while reading '{filename}': {e}")
