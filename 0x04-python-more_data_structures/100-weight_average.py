#!/usr/bin/python3


def weight_average(my_list=[]):
    """
    Calculates the weighted average of a list of tuples.

    Parameters:
    - my_list: Each tuple contains two values: element and weight.

    Returns:
    - float: Weighted average of the elements.
    """
    if not my_list:
        return 0

    # Using the sum func to calculate the weighted sum and sum of weights
    weighted_sum = sum(element * weight for element, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    # Avoid division by zero
    return float(weighted_sum / total_weight) if total_weight != 0 else 0
