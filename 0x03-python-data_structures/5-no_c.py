#!/usr/bin/python3


def no_c(my_string):
    """
    Remove all occurrences of 'c' and 'C' from a string.

    Args:
    - my_string (str): The input string.

    Returns:
    - A new string with all occurrences of 'c' and 'C' removed.
    """
    # Create a new list containing only characters that are not 'c' or 'C'
    filtered_chars = [char for char in my_string if char.lower() not in {'c', 'C'}]

    # Join the filtered characters to form a new string
    result_string = "".join(filtered_chars)

    # Return the modified string
    return (result_string)
