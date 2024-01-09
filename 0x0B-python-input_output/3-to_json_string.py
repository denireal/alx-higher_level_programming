#!/usr/bin/python3

# Author: Denyefa Wari

import json

def to_json_string(my_obj):
    """
    Convert a Python object to a JSON-formatted string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        str: The JSON-formatted string.
    """
    return json.dumps(my_obj)
