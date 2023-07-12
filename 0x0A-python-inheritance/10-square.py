#!/usr/bin/python3

"""
10-square
"""


class Square(Rectangle):
    def __init__(self, size):
        """
        Initializes a Square instance with private attribute size.
        Validates the size as a positive integer using integer_validator.
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square's dimensions.
        """
        return f"[Square] {self.__size}/{self.__size}"
