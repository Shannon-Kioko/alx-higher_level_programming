#!/usr/bin/python3

"""
8-class_to_json module
Contains function that creates a function that returns the
dictionary description
with a simple data structure suitable for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Get the dictionary description of an object with simple data
    structure for JSON serialization.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    description = {}
    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        if type(attr_value) in [list, dict, str, int, bool]:
            description[attr_name] = attr_value
    return description
