#!/usr/bin/python3
"""
Get a list of attributes and methods of an object.
"""


def lookup(obj):
    """
    Args:
        obj: Any Python object.

    Returns:
        list: List of strings representing the attributes
    and methods of the object.
    """
    return dir(obj)
