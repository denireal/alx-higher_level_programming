#!/usr/bin/python3
"""
Check if the given object is an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: Any Python object.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance of the class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
