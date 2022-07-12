#!/usr/bin/python3
"""A  class Rectangle that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Module of a rectangle


    Attributes:
        id (int): Describes the identity of each instance
        __width (int): Decribes the width of a rectangle
        __height (int): Describes the height of a rectangle
        __x (int): Describes the x position
        __y (int): Describes the y position
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle attributes


        Args:
            id (int): Describes the identity of each instance
            width (int): Decribes the width of a rectangle
            height (int): Describes the height of a rectangle
            x (int): Describes the x position
            y (int): Describes the y position


        Returns:
            None
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getting the width


        Returns:
            the width of a rectangle
        """
        return(self.__width)

    @property
    def height(self):
        """getting the height


        Returns:
            the height of a rectangle
        """
        return(self.__height)

    @property
    def x(self):
        """getting x


        Returns:
            the x position
        """
        return(self.__x)

    @property
    def y(self):
        """getting y


        Returns:
            the y position
        """
        return(self.__y)

    @width.setter
    def width(self, value):
        """setting the width


        Args:
            value (int):Describes the width of a rectangle


        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setting the height


        Args:
            value (int):Describes the height of a rectangle


        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setting x


        Args:
            value (int):Describes the x position


        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setting y


        Args:
            value (int):Describes the y position


        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates area of a rectangle


        Returns:
            the rectangle area
        """
        return(self.__width * self.__height)

    def display(self):
        """Prints in stdout the Rectangle instance with the character #
        
        
        Returns:
            None
        """
        for i in range(self.y):
            print()
        for j in range(self.height):
            for m in range(self.x):
                print(" ", end="")
            for n in range(self.width):
                print("#", end="")
                print()

    def __str__(self):
        """Represents the Rectangle objects as a string


        Returns:
            the 'informal' representing string
        """
        a, b, c = self.id, self.x, self.y
        d, e = self.width, self.height
        return("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))

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
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
    
    def to_dictionary(self):
        """
        Return:
            the dictionary representation of a Rectangle
        """
        return({"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y})
