#!/usr/bin/python3


def number_keys(a_dictionary):
    """
    Returns the number of keys in a given dictionary.

    Args:
    - a_dictionary (dict): The input dictionary.

    Returns:
    - int: The number of keys in the dictionary.
    """
    # Use len() on the keys of the dictionary to get the count
    num_keys = len(a_dictionary.keys())

    return (num_keys)
