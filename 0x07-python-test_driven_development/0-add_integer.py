#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number. Default is 98.

    Returns:
    - int: The sum of a and b, both casted to integers if they are floats.

    Raises:
    - TypeError: If a or b is not an integer or float.

    Example:
    >>> add_integer(5, 10.5)
    15
    >>> add_integer(8)
    106
    """
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the addition of a and b
    return (a + b)
