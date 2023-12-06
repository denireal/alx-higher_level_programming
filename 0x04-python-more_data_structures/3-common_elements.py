#!/usr/bin/python3


def common_elements(set_1, set_2):
    """
    Finds the common elements between two sets.

    Args:
    - set_1 (set): The first input set.
    - set_2 (set): The second input set.

    Returns:
    - set: A new set containing the common elements between set_1 and set_2.
    """
    # Use the intersection operator to find common elements
    common_elements_set = set_1 & set_2

    return (common_elements_set)
