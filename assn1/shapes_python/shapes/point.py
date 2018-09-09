#!/usr/bin/env python3

"""
Point

This class represents point objects that can be moved and copied
"""
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Point:
    def __init__(self, *args, **kwargs):
        try:
            self.__constructWithCoords(args[0], args[1])
        except IndexError:
            raise ShapeException("Invalid number of arguments for point construction")

    def __constructWithCoords(self, x1, y1):
        self.__x = x1
        self.__y = y1

        Validator.validatePoint(value=self, errorMessage="Point construction failed")

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

    def move(self, deltaX, deltaY):
        Validator.validateDouble(deltaX, "Invalid delta-x value")
        Validator.validateDouble(deltaY, "Invalid delta-y value")
        self.__x += deltaX
        self.__y += deltaY

    def copy(self):
        return Point(self.__x, self.__y)

    def __eq__(self, other):
        """Override the default comparison operator"""
        if isinstance(other, Point):
            return (self.__x == other.x and self.__y == other.y)
        return False

