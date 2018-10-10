#!/usr/bin/env python3

"""
Rectangle

This class represents rectangle objects that can be moved.
Users of a rectangle can also compute its area, height, and width.
"""
from shapes.line import Line
from shapes.point import Point
from shapes.shape import Shape
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Rectangle(Shape):
    def __init__(self, *args, **kwargs):
        if len(list(args)) == 4:
            center = Point.getCenterPoint(args[0], args[2])
            super().__init__(center, *args, **kwargs)
        else:
            super().__init__(*args, **kwargs)
        self.lines.append(Line(self.point1, self.point2))
        self.lines.append(Line(self.point2, self.point3))
        self.lines.append(Line(self.point3, self.point4))
        self.lines.append(Line(self.point4, self.point1))
        Rectangle.validateRectangle(self, "Rectangle is invalid")

    @staticmethod
    def validateRectangle(value, errorMessage):
        if not isinstance(value, Rectangle):
            raise ShapeException(errorMessage)

        Line.validateLine(value.line1, "Line 1 is not a valid line.")
        Line.validateLine(value.line2, "Line 2 is not a valid line.")
        Line.validateLine(value.line3, "Line 3 is not a valid line.")
        Line.validateLine(value.line4, "Line 4 is not a valid line.")

        Validator.validateLinesFormLoop([value.line1, value.line2, value.line3, value.line4], "Lines do not form an enclosed rectangle.")

        Validator.validateLinesFormRightAngles([value.line1, value.line2, value.line3, value.line4], "Lines do not form 90 degree angles.")

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
    def point4(self):
        return self.points[3]

    @property
    def line1(self):
        return self.lines[0]

    @property
    def line2(self):
        return self.lines[1]

    @property
    def line3(self):
        return self.lines[2]

    @property
    def line4(self):
        return self.lines[3]

    def computeWidth(self):
        return self.line1.computeLength()

    def computeHeight(self):
        return self.line2.computeLength()

    def computeArea(self):
        return self.computeWidth() * self.computeHeight()
