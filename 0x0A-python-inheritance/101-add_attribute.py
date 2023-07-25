#!/usr/bin/python3

"""
101-add_attribute with function to add new attribute
"""


def add_new_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it’s possible

    Args:
        object (__main__.MyClass): name of the object.
        attr_name ('str): name of the attribute.
        value (str): value of the attribute.

    Raises:
        TypeError:  if the object can’t have new attribute.
    """
    if not hasattr(obj, "__dict__") and not hasattr(obj, "__slots__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
