#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Function to multiply each element in a list by a specified num using map.

    Parameters:
    - my_list (list): The input list of numbers.
    - number (int): The number to multiply each element in the list.

    Returns:
    - list: A new list containing result of multiplying each element by the
    specified number.
    """
    # Use map function to apply the lambda function to each element in the list
    # The lambda function multiplies each element by the specified number
    result_list = list(map(lambda x: x * number, my_list))

    # Return the resulting list
    return result_list
