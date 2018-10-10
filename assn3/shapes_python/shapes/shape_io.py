#!/usr/bin/env python3

"""
Handles shape IO

Load and save shapes in a simple scripting format,
either to/from a string, stdin, or a file
"""
from shapes.shape_exception import ShapeException
from shapes.shape_factory import ShapeFactory


class ShapeIO:
    def loadShape(self, shape_string=None, file=None):
        if shape_string is None or file is None:
            raise ShapeException("Expected either a string or file for loadShape")
        if file:
            with open(file, "r") as myfile:
                shape_string = myfile.readlines()
        shape = self.parseString(shape_string)
        return ShapeFactory.build(shape.pop(0), shape)

    def parseString(self, shape_string):
        return shape_string.strip().split(delimiter=",")

    def saveShape(self, shape, file=None):
        string = shape.toString()
        if file: print(string, file=file)
        return string
