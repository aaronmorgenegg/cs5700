#!/usr/bin/env python3

"""
Circle

This class represents circle objects that can be moved and scaled.
Users of an circle can also compute its area and radius.
"""
from shapes.constants import PI
from shapes.ellipse import Ellipse
from shapes.shape_exception import ShapeException


class Circle(Ellipse):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Circle.validateCircle(self, "Circle is invalid")

    @staticmethod
    def validateCircle(value, errorMessage):
        Ellipse.validateEllipse(value, errorMessage)

        if value.axis1.computeLength() != value.axis2.computeLength():
            raise ShapeException(errorMessage)

    def computeRadius(self):
        return self.axis1.computeLength()

    def computeArea(self):
        return PI * (self.computeRadius()**2)

    def toString(self, name="circle"):
        return super().toString("circle")
