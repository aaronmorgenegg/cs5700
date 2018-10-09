#!/usr/bin/env python3

"""
Line

This class represents line objects that can be moved.
Users of a line can also get its length and slope.
"""
import math

from shapes.point import Point
from shapes.shape import Shape
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Line(Shape):
    def __init__(self, *args, **kwargs):
        if len(list(args)) == 2:
            center = Point.getCenterPoint(args[0], args[1])
            super().__init__(center, *args, **kwargs)
        else:
            super().__init__(*args, **kwargs)
        Line.validateLine(self, "Line is invalid")

    @staticmethod
    def validateLine(value, errorMessage):
        """
        Method that validates that a line is valid.

        :raises: ShapeException: If the line is invalid
        """
        if not isinstance(value, Line):
            raise ShapeException(errorMessage)
        Point.validatePoint(value.point1, "Invalid point1")
        Point.validatePoint(value.point2, "Invalid point2")
        Validator.validateLineHasLength(value, "A Line must have a length greater than 0")

    @property
    def point1(self):
        return self.points[0]

    @property
    def point2(self):
        return self.points[1]

    def computeLength(self):
        return math.sqrt( ((self.point1.x - self.point2.x)**2) + ((self.point1.y - self.point2.y)**2) )

    def computeSlope(self):
        numerator = self.point2.y - self.point1.y
        denominator = self.point2.x - self.point1.x
        try:
            return numerator/denominator
        except ZeroDivisionError:
            if numerator > 0:
                return float('inf')
            else:
                return float('-inf')
