#!/usr/bin/python3
"""Module for matrix division.

This module provides a function that divides all elements
of a matrix by a given number and returns a new matrix.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix: list of lists of integers or floats.
        div: number (int or float) used as divisor.

    Returns:
        A new matrix with each element divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix is not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(x, (int, float)) for row in matrix for x in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError(
            "Each row of the matrix must have the same size"
        )

    return [[round(x / div, 2) for x in row] for row in matrix]
