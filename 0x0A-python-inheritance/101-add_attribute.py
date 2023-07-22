#!/usr/bin/python3

"""
101-add_attribute
"""


def add_new_attribute(obj, attribute, value):
    """
    adds a new attribute to an object if it’s possible
    params:
        obj: the instance
        attribute: attribute to add to instance
        value: the value of newly added instance attribute

    Returns: the new attribute and value
    """
    if not hasattr(obj, "__dict__") and not hasattr(obj, "__slots__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
