#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """
    Deletes a key-value pair from a dictionary.

    Args:
    - a_dictionary (dict): The input dictionary.
    - key (str): The key to delete from the dictionary.

    Returns:
    - dict: The updated dictionary after deletion.
    """
    # Check if the key is present in the dict before attempting to delete
    if key in a_dictionary:
        # Delete the key-value pair
        del a_dictionary[key]

    return a_dictionary
