#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    Replaces occurrences of a specified value in a list.

    Args:
    - my_list (list): The input list.
    - search: The value to search for in the list.
    - replace: The value to replace occurrences of the search value.

    Returns:
    - list: A new list with occurrences of the search value replaced.
    """
    updated_list = []
    for element in my_list:
        if element != search:
            updated_list.append(element)
        else:
            updated_list.append(replace)
    return (updated_list)
