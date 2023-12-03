#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.

    Args:
    - matrix (list of lists): The matrix of integers to be printed.
      Defaults to an empty matrix if not provided.

    Returns:
    - None
    """
    # Iterate through each row in the matrix
    for row in matrix:
        # Print each integer in the row, separated by spaces
        print(' '.join('{:d}'.format(element) for element in row))
