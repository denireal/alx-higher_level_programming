#!/usr/bin/python3
"""
Module to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for current_row in range(1, n):
    row = [1]
    for current_element in range(1, current_row):
        row_append(triangle[current_row-1][current_element-1] +
                   triangle[current_row-1][current_element])
        row.append(1)
        triangle.append(row)

    return triangle
