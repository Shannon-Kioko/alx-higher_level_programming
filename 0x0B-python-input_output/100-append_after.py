#!/usr/bin/python3
"""
100-append_after module
Script that reads stdin line by line and computes metrics:
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a new string after the first occurrence of a search string
    in a file.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in the file.
        new_string (str): The string to append after the first occurrence
        of the search string.

    Returns:
        None
    """
    with open(filename, 'r') as file:
        content = file.read()

    index = content.find(search_string)
    if index != -1:
        index += len(search_string)
        new_content = content[:index] + new_string + content[index:]

        with open(filename, 'w') as file:
            file.write(new_content)
