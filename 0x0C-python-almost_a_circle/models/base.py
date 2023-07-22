#!/usr/bin/python3

""" models/base.py base of the classes in this project directory """


class Base:
    """
    This class will be the "base" of all other classes in this project.
    The goal of it is to manage the id attribute in all your future classes
    and to avoid duplicating the same code (and bugs).
    """

    __nb_objects = 0  # Private class attribute to manage id values

    def __init__(self, id=None):
        """
        Class constructor to initialize the object with an id.

        Parameters:
        id (int, optional): If provided, assigns the public instance
        attribute 'id' with this value.
        If not, increments the __nb_objects and assigns the new value
        to public instance attribute 'id'.

        Returns:
        None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
