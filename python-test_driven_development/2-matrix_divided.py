#!/usr/bin/python3
"""Module for matrix division."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix."""

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(x, (int, float)) for row in matrix for x in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(x / div, 2) for x in row] for row in matrix]
