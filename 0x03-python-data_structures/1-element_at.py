#!/usr/bin/python3


def element_at(my_list, idx):
    """
    Returns the element at the specified index in the list.

    Args:
    - my_list (list): The input list.
    - idx (int): The index of the element to retrieve.

    Returns:
    - The element at the specified index, or None if the index is out of bounds.
    """
    # Check if the index is out of bounds
    if 0 <= idx < len(my_list):
        return my_list[idx]

    # Return None for out-of-bounds index
    return None
