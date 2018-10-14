#!/usr/bin/env python3

"""
Composite Shape

This class represents composite shapes that contain other shapes.
Users of a composite shape can also compute its area, and can
add or remove shapes from the composite
"""
from shapes.shape import Shape
from shapes.shape_exception import ShapeException


class Composite(Shape):
    def __init__(self, *args, **kwargs):
        self.center = args[0]
        self.shapes = []
        for i in range(1, len(args)):
            self.addShape(args[i])
        Composite.validateComposite(self, "Composite is invalid")

    @staticmethod
    def validateComposite(value, errorMessage):
        if not isinstance(value, Composite):
            raise ShapeException(errorMessage)

        value.center.validate()
        for shape in value.shapes:
            shape.validate()

    def validate(self):
        Composite.validateComposite(self, "Composite is invalid")

    def getShape(self, index):
        try:
            return self.shapes[index]
        except IndexError:
            raise ShapeException('Index out of bounds for getShape({})'.format(index))

    def addShape(self, shape):
        shape.validate()
        self.shapes.append(shape)

    def removeShape(self, index):
        try:
            return self.shapes.pop(index)
        except IndexError:
            raise ShapeException('Index out of bounds for removeShape({})'.format(index))

    def clearShapes(self):
        self.shapes.clear()

    def move(self, deltaX, deltaY):
        self.center.move(deltaX, deltaY)
        for shape in self.shapes:
            shape.move(deltaX, deltaY)

    def computeArea(self):
        area = 0
        for shape in self.shapes:
            area += shape.computeArea()
        return area

    def toString(self, name="composite"):
        value = "{},{},begin".format(name, str(self.center))
        for shape in self.shapes:
            value += ",{}".format(shape.toString())
        return value+",end"

    def draw(self, graphics):
        for shape in self.shapes:
            shape.draw(graphics)

    def __eq__(self, other):
        if isinstance(other, Composite):
            return (self.center == other.center and self.shapes == other.shapes)
        return False
