#!/usr/bin/python3



def lookup(obj):
    """
    Get a list of attributes and methods of an object.

    Args:
        - obj: Any Python object.

    Returns:
        - list: A list of strings representing the attributes and methods of the object.
    """
    return dir(obj)
