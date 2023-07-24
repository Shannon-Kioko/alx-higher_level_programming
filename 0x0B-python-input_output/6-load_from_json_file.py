#!/usr/bin/python3
"""
6-load_from_json_file module
Contains a function that creates an Object from a “JSON file”
"""

import json

def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read and load the Python object.

    Returns:
        object: The Python object created from the JSON file.

    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
