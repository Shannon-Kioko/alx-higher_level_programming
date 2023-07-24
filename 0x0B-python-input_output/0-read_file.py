#!/usr/bin/python3
"""
'0-read_file' module
Contains a function that reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
     Read and print the contents of a text file (UTF-8) to stdout.

    Args:
        filename (str, optional): The name of the text file to
        read. Defaults to "".

    Returns:
        None.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
