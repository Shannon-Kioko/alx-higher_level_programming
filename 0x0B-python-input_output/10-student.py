#!/usr/bin/python3
"""
class Student that defines a student by: (based on 9-student.py)
Class contains public method to_json
"""


class Student:
    """
    A class that defines a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(attrs=None): Retrieves a dictionary
        representation of a Student instance.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get the dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute
            names to retrieve. Defaults to None.

        Returns:
            dict: A dictionary containing the specified
            attributes of the Student instance.
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
