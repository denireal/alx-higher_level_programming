#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Returns the element at the specified index in the given list.

    Args:
    - my_list (list): The list from which to retrieve the element.
    - idx (int): The index of the element to retrieve.

    Returns:
    - The element at the specified index, or None if index is out of bounds.
    """
    # Check if the index is -ve or >= length of the list
    if idx < 0 or idx >= len(my_list):
        return None

    # Return the element at the specified index
    return my_list[idx]
