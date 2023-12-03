#!/usr/bin/python3


def multiple_returns(sentence):
    """
    Returns a tuple containing the length of a string and its first character.

    Args:
    - sentence (str): The input string.

    Returns:
    - A tuple (length, first_character) where length is length of the string,
      and first_character is the first character of the string.
      If the input string is empty, returns (0, None).
    """
    # Check if the string is empty
    if sentence == "":
        return (0, None)

    # Return a tuple with the length and the first character of the string
    return (len(sentence), sentence[0])
