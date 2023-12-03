#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add corresponding elements of two tuples and return a new tuple.

    Args:
    - tuple_a (tuple, optional): The first tuple.
    - tuple_b (tuple, optional): The second tuple.

    Returns:
    - A new tuple containing the pairwise sum of corresponding elements
    """
    # Ensure both tuples have at least two elements by adding (0, 0) if needed
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Return a new tuple with the pairwise sum of corresponding elements
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
