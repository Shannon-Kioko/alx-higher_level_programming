#!/usr/bin/python3
"""Defines a class LockedClass"""


class LockedClass:
    """
    This class restricts the user from dynamically creating
    new instance attributes,
    except for the attribute named 'first_name'.

    Attributes:
        first_name (str): The first name of something.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of the LockedClass."""

        self.first_name = "first_name"
