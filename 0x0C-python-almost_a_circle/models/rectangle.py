# models/rectangle.py
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
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
