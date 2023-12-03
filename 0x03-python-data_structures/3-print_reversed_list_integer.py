#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    Print integers of a list in reverse order.

    Args:
    - my_list (list, optional): The list of integers to be printed
    in reverse order. Defaults to an empty list if not provided.

    Returns:
    - None
    """
    # Check if the provided argument is a list
    if isinstance(my_list, list):
        # Reverse the list in-place
        my_list.reverse()

        # Print each item in the reversed list
        for i in my_list:
            print("{:d}".format(i))
