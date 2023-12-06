#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    """
    Multiplies each element of the input list by the given number.

    Parameters:
    - my_list (list): List of elements to be multiplied.
    - number (int): The number to multiply each element by.

    Returns:
    - list: Resulting list after multiplication.
    """
    return list(map(lambda x: number * x, my_list))
