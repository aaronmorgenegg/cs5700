#!/usr/bin/env python3

"""
Handles shape IO

Load and save shapes in a simple scripting format,
either to/from a string, stdin, or a file
"""
from shapes.point import Point
from shapes.shape_exception import ShapeException
from shapes.shape_factory import ShapeFactory


class ShapeIO:
    def loadShape(self, string=None, file=None):
        if string is None and file is None:
            raise ShapeException("Expected either a string or file for loadShape")
        if file:
            with open(file, "r") as myfile:
                string = myfile.readlines()
        shape = self.parseString(string)
        return ShapeFactory.build(shape.pop(0), *shape)

    def parseString(self, string):
        parsed_string = string.strip().split(",")
        shape = [parsed_string.pop(0)]
        for i in range(0, len(parsed_string), 2):
            shape.append(Point(float(parsed_string[i]), float(parsed_string[i+1])))
        return shape

    def saveShape(self, shape, file=None):
        string = shape.toString()
        if file: print(string, file=file)
        return string
