#!/usr/bin/python3

"""
9-rectangle inheriting from 7-base_geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with private attributes W and H.
        Validates the W and H as positive integers using integer_validator.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of Rectangle instance.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string rep of the Rectangle's dimensions.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
