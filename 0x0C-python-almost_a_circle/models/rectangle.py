#!/usr/bin/python3

""" models/rectangle.py with validators"""
from models.base import Base

class Rectangle(Base):
    """
    Class Rectangle inherits from the Base class and represents a rectangle.

    Private instance attributes:
        __width: Width of the rectangle.
        __height: Height of the rectangle.
        __x: x-coordinate of the rectangle's position.
        __y: y-coordinate of the rectangle's position.

    Public instance methods:
        width: Getter and setter for the width attribute.
        height: Getter and setter for the height attribute.
        x: Getter and setter for the x attribute.
        y: Getter and setter for the y attribute.

    Parameters:
        width (int): Width of rectangle.
        height (int): Height of rectangle.
        x (int, optional): x-coordinate of the rectangle's position. Default = 0.
        y (int, optional): y-coordinate of the rectangle's position. Default = 0.
        id (int, optional): If provided, assigns public instance 
        attribute 'id' with this value.
        If not, increments the __nb_objects and assigns the new value
        to the public instance attribute 'id'.

    Returns:
        None
        """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """
        Returns the area value of the Rectangle instance.

        Formula: area = width * height

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle instance with the character '#' in stdout.

        Returns:
            None
        """
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """
        Returns a string rep of the Rectangle instance.

        Format: [Rectangle] (<id>) <x>/<y> - <width>/<height>

        Returns:
            str: The string representation of Rectangle instance.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
