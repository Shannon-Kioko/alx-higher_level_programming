#!/usr/bin/python3
"""
This is the 1-write_file
Contains a function that writes a string to a text file (UTF-8)
and returns numof char
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return the number
    of characters written.

    Args:
        filename (str, optional): The name of the text file to write.
        Defaults to "".
        text (str): The string to write to file.

    Returns:
        int: The numof characters written to the file.
    """
    try:
        with open(filename, mode='w', encoding='utf-8') as file:
            chars_written = file.write(text)
            return chars_written
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
