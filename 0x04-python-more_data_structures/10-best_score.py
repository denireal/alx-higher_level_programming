#!/usr/bin/python3


def best_score(a_dictionary):
    """
    Function to find and return the key with the highest value
    in a dictionary.

    Parameters:
    - a_dictionary (dict): The input dictionary.

    Returns:
    - str or None: The key with the highest value or None if the
    dictionary is empty.
    """
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # Use the max function with a key argument to find the key with
    # the maximum value
    # The key argument specifies a function to extract a comparison
    # key from each element
    max_key = max(a_dictionary, key=a_dictionary.get)

    # Return the key with the highest value
    return max_key
