#!/usr/bin/python3

import json


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        return super().default(obj)


def class_to_json(obj):
    """
    Convert a class object to a JSON-serializable dictionary.

    Args:
        obj: The class object to be converted.

    Returns:
        dict: A dictionary representing the serialized class.
    """
    return json.dumps(obj, cls=CustomEncoder)
