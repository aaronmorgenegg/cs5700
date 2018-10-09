#!/usr/bin/env python3

"""
Shape

Parent class for shapes. Consists of a set of points.
Shapes can be moved, scaled, and copied.
"""
from shapes.point import Point
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Shape:
    def __init__(self, *args, **kwargs):
        try:
            if not self.__constructWithPoints(list(args)):
                raise ShapeException("Shape construction failed")
        except IndexError:
            raise ShapeException("Invalid arguments for shape construction")

    def __constructWithPoints(self, points):
        try:
            self.center = points.pop(0)
            self.points = points
            self.lines = []
            Shape.validateShape(value=self, errorMessage="Invalid Shape")
            return True
        except ShapeException:
            return False

    @staticmethod
    def validateShape(value, errorMessage):
        if not isinstance(value, Shape):
            raise ShapeException(errorMessage)

        Point.validatePoint(value.center, "Center is not a valid line.")
        for point in value.points:
            Point.validatePoint(point, "Point is not a valid point.")

    def move(self, deltaX, deltaY):
        self.center.move(deltaX, deltaY)
        for point in self.points:
            point.move(deltaX, deltaY)

    def scale(self, factor):
        Validator.validatePositiveDouble(factor, "Scale Factor not a valid double")
        for point in self.points:
            dx = self.point.x - self.center.x
            dy = self.point.y - self.center.y
            point.x = dx * factor + self.center.x
            point.y = dy * factor + self.center.y

    def copy(self):
        pass # TODO

    def __eq__(self, other):
        """Override the default comparison operator"""
        if isinstance(other, Shape):
            return (self.center == other.center and self.points == other.points)
        return False

