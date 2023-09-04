#!/usr/bin/python3
"""A class defined Rectangle"""


class Rectangle:
    """defined class"""

    def __init__(self, width=0, height=0):
        """initializing the rectangle components
        Args:
            width: the rectangle width
            height: the rectangle height
        Raises:
            TypeError: if size is not int
            ValueError: if size is negative
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self) -> str:
        if self.__width == 0 or self.height == 0:
            return ""
        rectangle = ""
        row = '#' * self.__width
        rectangle = (row + "\n") * (self.__height - 1)
        rectangle += row
        return rectangle

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
