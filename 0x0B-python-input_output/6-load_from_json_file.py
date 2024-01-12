#!/usr/bin/python3
""" Module for creating a Python object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Retrieve a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to be loaded.

    Returns:
        object: The Python object generated from the JSON data.

    Raises:
        Exception: If the decoding of the object from the JSON file fails.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
