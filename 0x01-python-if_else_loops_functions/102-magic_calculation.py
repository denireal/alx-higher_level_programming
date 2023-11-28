#!/usr/bin/python3

def magic_calculation(a, b, c):
    """
    Performs a magic calculation based on the values of a, b, and c.

    Parameters:
    - a (int): First input value.
    - b (int): Second input value.
    - c (int): Third input value.

    Returns:
    - int: Result of the magic calculation.
    """
    if a < b and c > b:
        # If a is less than b and c is greater than b, return the sum of a and b
        return a + b
    elif a < b:
        # If a is less than b, return c
        return c
    else:
        # Otherwise, return the result of (a * b) - c
        return (a * b) - c
