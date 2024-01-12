#!/usr/bin/python3
"""
Convert a class object to a JSON-serializable dictionary.
"""


def class_to_json(obj):
    """
    Convert a class object to a JSON-serializable dictionary.

    Args:
        obj: The class object to be converted.

    Returns:
        dict: A dictionary representing the serialized class.
    """
    if hasattr(obj, "__dict__"):
        # Recursively convert attributes to JSON
        return {key:
                class_to_json(value) for key, value in obj.__dict__.items()}
    elif isinstance(
            obj, (int, float, str, bool, list, tuple, dict, type(None))):
        # Handle basic types directly
        return obj
    else:
        # For other custom types, you might want to provide more specific logic
        return str(obj)
