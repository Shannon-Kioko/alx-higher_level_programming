#!/usr/bin/python3
"""
11-student module
Contains class based on 10-student.py, with public method reload_from_json
"""


class Student:
    """
    A class that defines a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(attrs=None): Retrieves a dictionary representation of
        a Student instance.
        reload_from_json(json): Replaces all attributes of the
        Student instance.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get the dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names
            to retrieve. Defaults to None.

        Returns:
            dict: A dictionary containing the specified attributes of
            the Student instance.
        """
        if attrs is None:
            attrs = [attr_name for attr_name in dir(self)
                     if not attr_name.startswith('__')]
        description = {}
        for attr_name in attrs:
            if hasattr(self, attr_name):
                attr_value = getattr(self, attr_name)
                if type(attr_value) in [str, int]:
                    description[attr_name] = attr_value
        return description

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with the
        provided JSON dictionary.

        Args:
            json (dict): A dictionary with attribute names
            as keys and corresponding values.

        Returns:
            None
        """
        for attr_name, attr_value in json.items():
            if hasattr(self, attr_name):
                setattr(self, attr_name, attr_value)
