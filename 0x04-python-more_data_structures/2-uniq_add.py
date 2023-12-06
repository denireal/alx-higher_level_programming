#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    Calculates the sum of unique elements in a given list.

    Args:
    - my_list (list): The input list.

    Returns:
    - int: The sum of unique elements in the list.
    """

    unique_set = set(my_list)
    total = 0
    for number in unique_set:
        total += number
    return total
