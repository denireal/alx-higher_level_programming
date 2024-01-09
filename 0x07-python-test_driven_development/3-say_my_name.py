#!/usr/bin/python3
"""
Module for the say_my_name function.
"""


def say_my_name(first_name, last_name=""):
    """Prints a formatted message with the given first and last names.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Returns:
        None
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
