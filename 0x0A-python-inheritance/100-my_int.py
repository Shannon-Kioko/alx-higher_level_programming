#!/usr/bin/python3

"""
100-my_int inherits from Int class
"""


class MyInt(int):
    """
    Inherits from Int class
    """
    def __eq__(self, other):
        """
        Overrides the '==' operator to invert the og behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides this '!=' operator to invert its behavior.
        """
        return super().__eq__(other)
