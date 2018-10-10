#!/usr/bin/env python3

"""
Ellipse

This class represents ellipse objects that can be moved and scaled.
Users of an ellipse can also compute its area.
"""
from shapes.constants import PI
from shapes.line import Line
from shapes.shape import Shape
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Ellipse(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lines.append(Line(self.center, self.point1))
        self.lines.append(Line(self.center, self.point2))
        Ellipse.validateEllipse(self, "Ellipse is invalid")

    @staticmethod
    def validateEllipse(value, errorMessage):
        if not isinstance(value, Ellipse):
            raise ShapeException(errorMessage)

        Line.validateLine(value.axis1, "Axis1 is not a valid line")
        Line.validateLine(value.axis2, "Axis2 is not a valid line")

        if value.computeArea() <= 0:
            raise ShapeException(errorMessage)

        Validator.validateLinesFormRightAngles([value.axis1, value.axis2], "Axis are not perpendicular")

    def validate(self):
        return Ellipse.validateEllipse(self, "Ellipse is invalid")

    @property
    def axis1(self):
        return self.lines[0]

    @property
    def axis2(self):
        return self.lines[1]

    @property
    def point1(self):
        return self.points[0]

    @property
    def point2(self):
        return self.points[1]

    def computeArea(self):
        return PI * self.axis1.computeLength() * self.axis2.computeLength()

    def toString(self, name="ellipse"):
        return super().toString("ellipse")
