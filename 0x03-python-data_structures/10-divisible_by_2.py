#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """
    Returns a list of boolean values

    Args:
    - my_list (list): The input list of integers.

    Returns:
    - A list of boolean values, where each element corresponds to
      whether the corresponding element in the input list is divisible by 2.
    """
    # Use a more descriptive variable name than 'num'
    return ([num % 2 == 0 for num in my_list])
