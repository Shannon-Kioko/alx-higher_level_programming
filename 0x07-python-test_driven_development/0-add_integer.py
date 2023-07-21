#!/usr/bin/python3
"""Module on tests with addition"""
def add_integer(a, b=98):


    """
    Adds two int integers

    Args:
        a (float or int): first number to sum up. If it's of type int
        b: second paramter to add, type int

    Raises:
        TypeError: If both parameters are not int or float

    Returns:
        int: sum of a and b

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
