#!/usr/bin/python3
"""""This module create a rectangle"""


class Rectangle:
    """
    class that generate a rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Constructor initialize the class rectangle
        Keyword Arguments:
            width {int} -- width of the rectangle (default: {0})
            height {int} -- height of the rectangle (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter function of width
        Returns:
            int -- width fo the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function to width
        Arguments:
            value {int} -- [valeu of width]
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter function to height
        Returns:
            int -- height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function os height
        Arguments:
            value {int} -- Value of height
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Generate area of the rectangle
        Returns:
            Int -- total area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Find the perimeter of a rectangle
        Returns:
            int -- total perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Method that get string representation rectangle
        Returns:
            string -- string representation
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for row in range(self.__height):
            for col in range(self.__width):
                string = string + '#'
            string = string + '\n'
        return string[:-1]

    def __repr__(self):
        """Rerurn string of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Delete instance of the rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
