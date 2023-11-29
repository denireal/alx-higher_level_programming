#!/usr/bin/python3


def remove_char_at(str, n):
    """
    Removes a character at the specified index from the given string.

    Parameters:
    - str (str): The input string from which a character ll be removed.
    - n (int): The index of the character to be removed.

    Returns:
    - str: Modified string after removing character at d specific index.
    """
    if n < 0:
        return (str)
    else:
        result_str = str[:n] + str[n + 1:]
        return (result_str)
