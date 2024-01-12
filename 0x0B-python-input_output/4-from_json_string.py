#!/usr/bin/python3

# Author: Denyefa Wari
"""Convert a JSON-formatted string to a Python object."""

import json


def from_json_string(my_str):
    """
    Convert a JSON-formatted string to a Python object.

    Args:
        my_str (str): The JSON-formatted string to be converted.

    Returns:
        object: The Python object.
    """
    return json.loads(my_str)
