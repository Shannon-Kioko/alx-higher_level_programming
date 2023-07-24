#!/usr/bin/python3
"""
5-save_to_json_file module
Contains function that saves a python object to a text file using its JSON representation.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a text file using its JSON representation.

    Args:
        my_obj: The Python object to be saved.
        filename (str): The name of the text file to save the JSON representation.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
