#!/usr/bin/env python3

"""
Image Shape

This class represents embedded image shapes that contain an image.
Users of an image shape can also compute its area
"""
from shapes.line import Line
from shapes.shape import Shape
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Image(Shape):
    def __init__(self, *args, **kwargs):
        self.center = args[0]
        self.points = [args[1], args[2]]
        self.source = args[3]
        Image.validateImage(self, "Image is invalid")

    @staticmethod
    def validateImage(value, errorMessage):
        if not isinstance(value, Image):
            raise ShapeException(errorMessage)

        value.center.validate()
        value.points[0].validate()
        value.points[1].validate()
        Line(value.points[0], value.points[1])

        Validator.validateSource(value.source)

    def validate(self):
        return Image.validateImage(self, "Image is invalid")

    @property
    def point1(self):
        return self.points[0]

    @property
    def point2(self):
        return self.points[1]

    def computeWidth(self):
        return self.point2.x - self.point1.x

    def computeHeight(self):
        return self.point1.y - self.point2.y

    def computeArea(self):
        return self.computeWidth() * self.computeHeight()

    def toString(self, name="image"):
        return super().toString(name) + ", {}".format(self.source)
