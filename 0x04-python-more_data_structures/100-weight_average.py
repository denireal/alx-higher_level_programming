#!/usr/bin/python3


def weight_average(my_list=[]):
    """
    Function to calculate the weighted average of a list of tuples.

    Parameters:
    - my_list (list): The input list of tuples

    Returns:
    - float: Returns 0 if the list is empty or None.
    """
    # Check if the list is empty or None
    if len(my_list) == 0 or my_list is None:
        return 0
    
    # Variables to store the sum of weights, sum of weighted products
    # and the weighted average
    sum_weights = sum_weighted_products = weighted_average = 0

    # Iterate through each tuple in the list
    for tuple_item in my_list:
        # Extract values from the tuple
        weight, value = tuple_item

        # Update the sum of weights
        sum_weights += weight

        # Calculate the weighted product for the current tuple
        weighted_product = weight * value

        # Update the sum of weighted products
        sum_weighted_products += weighted_product

    # Calculate the weighted average
    weighted_average = sum_weighted_products / sum_weights

    # Return the weighted average
    return weighted_average
