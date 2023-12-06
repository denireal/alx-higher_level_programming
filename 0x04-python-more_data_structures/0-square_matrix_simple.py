#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    Computes the square of each element in a given matrix.

    Args:
    - matrix (list of lists): The input matrix.

    Returns:
    - (list of lists): A new matrix where each element is the square of the
    - corresponding element in the input matrix.
    """
    squared_matrix = [[element**2 for element in row] for row in matrix]
    return (squared_matrix)
