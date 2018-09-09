#!/usr/bin/env python3

"""
Circle

This class represents circle objects that can be moved and scaled.
Users of an circle can also compute its area and radius.
"""

import math

class Circle(Ellipse):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Validator.validateCircle(self, "Circle is invalid")

    def computeRadius():
        pass # TODO:

    def computeArea():
        return PI * (computeRadius()**2)

