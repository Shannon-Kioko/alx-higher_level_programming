#!/usr/bin/python3
"""
Module for performing matrix operations.

This module provides functions to perform various operations
on matrices, including division of elements by a given number.

"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number
    and round to 2 decimal places.

    Args:
        matrix (list of lists): A matrix represented as a
        list of lists of integers or floats.
        div (int or float): The number to divide each element of the matrix by.

    Returns:
        list of lists: A new matrix where all elements are divided
        by the given number and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and
    all(isinstance(elem, (int, float)) for elem in row) for row in matrix):

        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    # Check if each row of the matrix has the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
