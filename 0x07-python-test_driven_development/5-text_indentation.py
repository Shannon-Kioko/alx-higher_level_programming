#!/usr/bin/python3
"""
Module with one function text_indentation
"""


def text_indentation(text):

    """
    Print a given text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
