#!/usr/bin/python3
"""
8-rectangle based on 7-rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
