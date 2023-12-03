#!/usr/bin/python3


def max_integer(my_list=[]):
    """
    Returns the maximum integer in a list.

    Args:
    - my_list (list): The input list of integers.

    Returns:
    - The maximum integer in the list, or None if the list is empty.
    """
    if my_list is None or len(my_list) == 0:
        return (None)
    else:
        my_list.sort()
        return (my_list[-1])
