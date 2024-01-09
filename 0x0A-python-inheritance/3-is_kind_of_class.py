#!/usr/bin/python3
"""
Check if the given object is an instance or
a subclass instance of the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: Any Python object.
        a_class: The class to check against.

    Returns:
        bool: True if the object is an instance or subclass instance
        of the class, False otherwise.
    """
    return isinstance(obj, a_class)
