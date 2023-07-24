#!/usr/bin/python3
"""
4-from_json_string modyle
Contains functions that returns an object represented by JSON string
"""

import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python data structure (object).

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python data structure represented by the JSON string.

    """
    return json.loads(my_str)
