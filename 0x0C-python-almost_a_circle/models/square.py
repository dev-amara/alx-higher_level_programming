#!/usr/bin/python3
"""A  class Square that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Module of a square


    Use all attributes of Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the rectangle attributes


        Args:
            id (int): Describes the identity of each instance
            x (int): Describes the x position
            y (int): Describes the y position
            size(int): Describes the length of a square

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getting the size


        Returns:
            the length of a square
        """
        return(self.width)
    
    """The width and height must be assigned to the value of size"""
    @size.setter
    def size(self, value):
        """setting the size


        Args:
            value (int):Describes the length of a square


        Returns:
            None
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Represents the Square objects as a string


        Returns:
            the 'informal' representing string
        """
        a, b, c = self.id, self.x, self.y
        d = self.width
        return("[Square] ({}) {}/{} - {}".format(a, b, c, d))

    def update(self, *args, **kwargs):
        """ 'def update(self, *args):' alone assigns an argument to each attribute
        'def update(self, *args, **kwargs):' assigns a key/value argument to attributes


        Args:
            args(list): no-keyword argument, order is important
            kwargs(dict): key-worded argument, order is not important

        Returns:
            None
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
    
    def to_dictionary(self):
        """
        Return:
            the dictionary representation of a Square
        """
        return({"id": self.id, "size": self.size, "x": self.x, "y": self.y})
