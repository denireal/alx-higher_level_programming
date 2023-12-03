#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """
    Delete the element at the specified index in the input list.

    Args:
    - my_list (list): The input list.
    - idx (int): The index at which to delete the element.

    Returns:
    - The modified list after deleting the element at the specified index,
      or the original list if the index is out of bounds.
    """
    # Check if the index is out of bounds
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        # Delete the element at the specified index
        del my_list[idx]

        # Return the modified list
        return (my_list)
