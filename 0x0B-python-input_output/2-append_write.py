#!/usr/bin/python3
"""
2-append_write module
Contains function that appends a string at the end of a text file (UTF-8)
and returns the number of characters added.

"""
def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF-8) and return the number of characters added.

    Args:
        filename (str, optional): The name of the text file to append to. Defaults to "".
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.

    """
    try:
        with open(filename, mode='a', encoding='utf-8') as file:
            chars_added = file.write(text)
            return chars_added
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
  
