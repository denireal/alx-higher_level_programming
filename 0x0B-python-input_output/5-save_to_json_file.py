#!/usr/bin/python3

import json

def save_to_json_file(*args):
    """
    Save a Python object to a JSON-formatted file.

    Args:
        args: Variable-length arguments where args[0] is the Python object to be saved
              and args[1] is the name of the file to save the JSON data to.
    """
    with open(args[1], 'w', encoding="utf-8") as f:
        json.dump(args[0], f)
