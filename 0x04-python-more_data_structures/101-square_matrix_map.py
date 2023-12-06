#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    """
    Takes a 2D matrix as input and returns a new matrix where each element
    is the square of the corresponding element in the input matrix.

    Parameters:
    - matrix (list of lists): The input 2D matrix.

    Returns:
    - list of lists: The resulting matrix with each element squared.
    """
    # Using the map function to apply a lambda function to each row in the
    # matrix
    # The lambda function squares each element in the row
    # The outer map function applies this process to each row in the matrix
    # The result is a new matrix with elements squared
    return list(map(lambda x: list(map(lambda y: y * y, x)), matrix))
