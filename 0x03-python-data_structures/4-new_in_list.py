#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specified index with a new element.

    Args:
    - my_list (list): The original list.
    - idx (int): The index at which to replace the element.
    - element: The new element to be placed at the specified index.

    Returns:
    - A new list with the specified element replaced, or the original list
    - if the index is out of bounds.
    """
    # Check if the index is out of bounds
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    # Create a copy of the original list to avoid modifying it in-place
    modified_list = [x for x in my_list]

    # Replace the element at the specified index with the new element
    modified_list[idx] = element

    # Return the modified list
    return (modified_list)
