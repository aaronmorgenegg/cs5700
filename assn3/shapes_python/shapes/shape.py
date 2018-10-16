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
        points = list(args)
        if len(points) < 1:
            raise ShapeException('No points provided during shape construction')
        self.center = points.pop(0)
        self.points = points
        self.lines = []
        Shape.validateShape(value=self, errorMessage="Invalid Shape")

    @staticmethod
    def validateShape(value, errorMessage):
        if not isinstance(value, Shape):
            raise ShapeException(errorMessage)

        Point.validatePoint(value.center, "Center <{}> is not a valid point.".format(value.center))
        for point in value.points:
            Point.validatePoint(point, "Point <{}> is not a valid point.".format(point))

    def validate(self):
        return Shape.validateShape(self, "Shape is invalid")

    def move(self, deltaX, deltaY):
        self.center.move(deltaX, deltaY)
        for point in self.points:
            point.move(deltaX, deltaY)

    def scale(self, factor):
        Validator.validatePositiveDouble(factor, "Scale Factor not a valid double")
        for point in self.points:
            dx = point.x - self.center.x
            dy = point.y - self.center.y
            point.x = dx * factor + self.center.x
            point.y = dy * factor + self.center.y

    def copy(self):
        pass # TODO

    def __eq__(self, other):
        """Override the default comparison operator"""
        if isinstance(other, Shape):
            return (self.center == other.center and self.points == other.points)
        return False

    def toString(self, name="shape"):
        value = "{},{}".format(name, str(self.center))
        for point in self.points:
            value += ",{}".format(str(point))
        return value

    def draw(self, graphics):
        points = []
        for point in self.points:
            points.append([point.x, point.y])

        shape = graphics.Polygon(points, fill=None)
        graphics.gca().add_patch(shape)
        graphics.axis('scaled')

    def __str__(self):
        return self.toString()
