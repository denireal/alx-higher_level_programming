#!/usr/bin/python3
"""
Module defining a matrix_divided function for dividing matrices.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): A matrix (list of lists) of integers/floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with each element rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not valid or if div is not a number.
        ZeroDivisionError: If div is 0.
    """

    # Check if matrix is a valid matrix
    if (
        not isinstance(matrix, list) or
        matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(
            isinstance(elm, (int, float))
            for elm in [num for row in matrix for num in row])
    ):
        raise TypeError("must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and round each element to 2 decimal places
    return [
        list(map(lambda x: round(x / div, 2), row))
        for row in matrix
    ]
