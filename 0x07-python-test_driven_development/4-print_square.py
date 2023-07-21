#!/usr/bin/python3
"""
Module 4-print_square, has one function,
prints a square with #
"""
def print_square(size):
    """
    Print a square with the character '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size % 1 != 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
