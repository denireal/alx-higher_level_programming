#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replaces the element at the specified index in the given list.

    Args:
    - my_list (list): The list in which to replace the element.
    - idx (int): The index of the element to replace.
    - element: The new element to be placed at the specified index.

    Returns:
    - The modified list after replacing the element, or the original list
    """
    # Check if the index is out of bounds
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    # Replace the element at the specified index with the new element
    my_list[idx] = element

    # Return the modified list
    return (my_list)
