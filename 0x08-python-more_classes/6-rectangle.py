#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of a rectangle (based on 5-rectangle.py).

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Width getter.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Height getter.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Width setter.

        Args:
            value (int): Width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Height setter.

        Args:
            value (int): Height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: The rectangle represented by the character '#'.
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        # Remove the last newline character
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: The rectangle representation.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of the class."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
