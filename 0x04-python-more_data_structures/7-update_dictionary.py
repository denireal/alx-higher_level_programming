#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """
    Updates a dictionary with a key-value pair.

    Args:
    - a_dictionary (dict): The input dictionary.
    - key: The key to update or add.
    - value: The value to set for the key.

    Returns:
    - dict: The updated dictionary.
    """
    # Check if the key is not in the dictionary
    if key not in a_dictionary:
        # Add the key-value pair
        a_dictionary[key] = value
    else:
        # Use a while loop to find the matching key and update its value
        existing_key_iter = iter(a_dictionary)
        while True:
            try:
                existing_key = next(existing_key_iter)
                if existing_key == key:
                    a_dictionary[existing_key] = value
                    break
            except StopIteration:
                break

    return (a_dictionary)
