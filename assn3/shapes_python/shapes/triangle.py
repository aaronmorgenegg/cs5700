#!/usr/bin/env python3

"""
Triangle

This class represents triangle objects that can be moved.
Users of a triangle can also compute its area.
"""

import math

from shapes.line import Line
from shapes.point import Point
from shapes.shape import Shape
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Triangle(Shape):
    def __init__(self, *args, **kwargs):
        if len(list(args)) == 3:
            center = Point.getCenterPoint(Point.getCenterPoint(args[0], args[1]), args[2])
            super().__init__(center, *args, **kwargs)
        else:
            super().__init__(*args, **kwargs)
        self.lines.append(Line(self.point1, self.point2))
        self.lines.append(Line(self.point2, self.point3))
        self.lines.append(Line(self.point3, self.point1))
        Triangle.validateTriangle(self, "Triangle is invalid")

    @staticmethod
    def validateTriangle(value, errorMessage):
        if not isinstance(value, Triangle):
            raise ShapeException(errorMessage)

        Line.validateLine(value.line1, "Line 1 has is not a valid line.")
        Line.validateLine(value.line2, "Line 2 has is not a valid line.")
        Line.validateLine(value.line3, "Line 3 has is not a valid line.")

        Validator.validateSlopesAreDifferent([value.line1, value.line2, value.line3], "Angles of lines form an invalid triangle")

        Validator.validateLinesFormLoop([value.line1, value.line2, value.line3], "Lines do not form an enclosed triangle")

    @property
    def point1(self):
        return self.points[0]

    @property
    def point2(self):
        return self.points[1]

    @property
    def point3(self):
        return self.points[2]

    @property
    def line1(self):
        return self.lines[0]

    @property
    def line2(self):
        return self.lines[1]

    @property
    def line3(self):
        return self.lines[2]

    def computeArea(self):
        """Compute area using Heron's formula"""
        a = self.line1.computeLength()
        b = self.line2.computeLength()
        c = self.line3.computeLength()
        s = (a+b+c)/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))

