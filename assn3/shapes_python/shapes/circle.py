#!/usr/bin/env python3

"""
Circle

This class represents circle objects that can be moved and scaled.
Users of an circle can also compute its area and radius.
"""
from shapes.constants import PI
from shapes.ellipse import Ellipse
from shapes.validator import Validator


class Circle(Ellipse):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Validator.validateCircle(self, "Circle is invalid")

    def computeRadius(self):
        return self.axis1.computeLength()

    def computeArea(self):
        return PI * (self.computeRadius()**2)

