#!/usr/bin/env python3

"""
Point

This class represents point objects that can be moved and copied
"""

from shapes.validator import Validator

class Point:
    def __init__(self, *args, **kwargs):
        self.__x = args[0]
        self.__y = args[1]
        
        Validator.validatePoint(self, "Point invalid")

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

    def move(deltaX, deltaY):
        Validator.validateDouble(deltaX, "Invalid delta-x value")
        Validator.validateDouble(deltaY, "Invalid delta-y value")
        self.x += deltaX
        self.y += deltaY

    def copy():
        return self.__deepcopy__()

    def __eq__(self, other):
        """Override the default comparison operator"""
        if isinstance(other, Point):
            return (self.x == other.x and self.y == other.y)
        return False

