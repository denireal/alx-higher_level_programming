#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """
    Function to delete entries from a dictionary based on a specified value.

    Parameters:
    - a_dictionary (dict): The input dictionary.
    - value: The value to match and delete from the dictionary.

    Returns:
    - dict: Modified dictionary after deleting entries with specified value.
    """
    # Create a list to store keys to be deleted
    keys_to_delete = []

    # Iterate through the items in the dictionary
    for key, key_value in a_dictionary.items():
        # Check if the value matches the specified value
        if key_value == value:
            # Add the key to the list of targets for deletion
            keys_to_delete.append(key)

    # Iterate through the list of keys_to_delete and delete corresponding
	# entries from the dictionary
    for x in keys_to_delete:
        del a_dictionary[x]

    # Return the modified dictionary
    return a_dictionary
