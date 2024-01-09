#!/usr/bin/python3
"""
Check if the given object is a subclass instance of the specified class.
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: Any Python object.
        a_class: The class to check against.

    Returns:
        bool: True if the object is a subclass instance, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
