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

    punctuation_chars = set('.?:')
    line = ""
    for char in text:
        line += char
        if char in punctuation_chars:
            print(line.strip())
            line = ""
    if line:
        print(line.strip())
