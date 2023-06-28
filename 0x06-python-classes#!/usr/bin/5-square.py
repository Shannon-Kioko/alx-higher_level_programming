#!/usr/bin/python3

"""
Module: 5
"""

class Square:
    """
    Represents a square shape with a given size.

    Attributes:
        size (int): The size of the square's sides.

    Methods:
        __init__(size): Initializes a Square instance with a specified size.
        area(): Calculates and returns the area of the square.
        my_print(): Prints a visual representation of the square.
    """

    def __init__(self, size=0):
        """
        Inits a Square instance with a specified size.

        Args:
            size (int): The size of the square's sides (default is 0).

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square's sides.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a visual representation of the square.

        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
