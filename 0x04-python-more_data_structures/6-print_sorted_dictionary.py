#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    Prints the key-value pairs of a dictionary in sorted order based on keys.

    Args:
    - a_dictionary (dict): The input dictionary.
    """
    # Iterate over the keys in sorted order and print key-value pairs
    for sorted_key in sorted(a_dictionary):
        print("{:s}: {}".format(sorted_key, a_dictionary[sorted_key]))
