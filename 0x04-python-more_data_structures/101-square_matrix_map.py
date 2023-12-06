#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    """
    Function to square each element in a matrix using the map function.

    Parameters:
    - matrix (list of lists): The input matrix.

    Returns:
    - list of lists: A new matrix with each element squared.
    """
    # Use the map function to apply the inner lambda function to each element
    # in each row
    # The inner lambda function squares each element in a row
    # The outer lambda function applies the inner lambda function to each row
    # in the matrix
    squared_matx = list(map(lambda x: list(map(lambda y: y * y, x)), matrix))

    # Return the resulting squared matrix
    return squared_matx
