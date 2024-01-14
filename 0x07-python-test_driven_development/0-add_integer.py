#!/usr/bin/python3
"""
This script defines a function add_integer(a, b=98)
that performs integer addition.
"""


def add_integer(a, b=98):
    """
    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.
    Raises:
        TypeError: If either a or b is not an integer or a float.
    Returns:
        int: The sum of a and b as an integer.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    # Convert a and b to integers before performing addition
    a = int(a)
    b = int(b)

    return (a + b)
