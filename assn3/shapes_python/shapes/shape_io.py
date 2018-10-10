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
        shape = self.parse(string)
        return ShapeFactory.build(shape.pop(0), *shape)

    def parse(self, string):
        parsed_string = string.strip().split(",")
        shape_tree = self.parseShapeTree(parsed_string)
        return self.buildShapes(shape_tree)

    def parseShapeTree(self, parsed_string):
        shape_tree = [parsed_string.pop(0)]
        while len(parsed_string) > 0:
            try:
                shape_tree.append(Point(float(parsed_string[0]), float(parsed_string[1])))
                parsed_string = parsed_string[2:]
            except ValueError: # Not a number, ie shapename or begin/end composite
                shape_tree.append(parsed_string.pop(0))

        return shape_tree

    def buildShapes(self):
        # ['composite',0,0,'begin','triangle',1,1,2,2,4,4,'end']
        pass

    def saveShape(self, shape, file=None):
        string = shape.toString()
        if file: print(string, file=file)
        return string
