#!/usr/bin/python3

"""
9-student module
Contains a class Student that defines a student and methods to retrieve a dict rep
of the Student instance
"""


class Student:
    """
    A class that defines a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(): Retrieves a dictionary representation of a Student instance.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
    """
      Get the dictionary description of an object with simple data structure for JSON serialization.

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
