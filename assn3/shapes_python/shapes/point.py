#!/usr/bin/env python3

"""
Point

This class represents point objects that can be moved and copied
"""
import math

from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Point:
    def __init__(self, *args, **kwargs):
        try:
            self.__constructWithCoords(args[0], args[1])
        except IndexError:
            raise ShapeException("Invalid arguments for point construction")

    def __constructWithCoords(self, x1, y1):
        self.__x = x1
        self.__y = y1

        self.validatePoint(self, errorMessage="Point construction failed")

    @staticmethod
    def validatePoint(value, errorMessage):
        """
        Method that validates that value is a valid point

        :raises: ShapeException: If value is not a valid point
        """
        if not isinstance(value, Point):
            raise ShapeException(errorMessage)
        Validator.validateDouble(value.x, "Invalid x-location")
        Validator.validateDouble(value.y, "Invalid y-location")

    def validate(self):
        return Point.validatePoint(self, "Point is invalid")

    @staticmethod
    def getCenterPoint(point1, point2):
        """Return the point inbetween point1 and point2"""
        return Point((point1.x+point2.x)/2, (point1.y+point2.y)/2)

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
            return math.isclose(self.__x, other.x) and math.isclose(self.__y, other.y)
        return False

    def toString(self):
        return str(self)

    def __str__(self):
        return "{},{}".format(self.x, self.y)

