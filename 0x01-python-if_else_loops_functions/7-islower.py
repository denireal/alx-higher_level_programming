#!/usr/bin/python3

"""
Author: Wari Denyefa
Description: This script defines a function islower that
checks whether a given character is lowercase.
"""

def islower(c):
    """Checks for lowercase

    Args:
        c: a single character argument

    Returns:
        True: if c is lowercase
        False: if c is not lowercase
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False
