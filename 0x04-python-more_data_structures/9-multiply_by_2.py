#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    Function to multiply each value in a given dictionary by 2.

    Parameters:
    - a_dictionary (dict): The input dictionary to be modified.

    Returns:
    - dict: A new dictionary with the values multiplied by 2.
    """
    # Create copy of input dictionary to avoid modifying the original
    updated_dict = a_dictionary.copy()

    # Iterate through key-value pairs in the dictionary
    for key, value in updated_dict.items():
        # Multiply each value by 2
        updated_dict[key] = value * 2

    # Return the updated dictionary
    return updated_dict
