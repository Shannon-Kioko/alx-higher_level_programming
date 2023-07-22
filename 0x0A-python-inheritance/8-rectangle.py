#!/usr/bin/python3
"""
8-rectangle based on 7-rectangle

7-base_geometry
"""


class BaseGeometry:
    """
    Base class for geometry-related operations.
    """
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value if an integer and greater than 0.
        Raises TypeError or ValueError based on failed validation.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    A class rectangle and inherits from BaseGeometry.

    params:
    BaseGeometry (class): base class that increments each time
    an instance is created
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with private attributes;
        width and height.
        Validates the width and height as positive integers,
        using integer_validator of the
        BaseGeometry class.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
