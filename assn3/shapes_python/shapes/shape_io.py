#!/usr/bin/env python3

"""
Handles shape IO

Load and save shapes in a simple scripting format,
either to/from a string, stdin, or a file
"""
from shapes.point import Point
from shapes.shape_exception import ShapeException
from shapes.shape_factory import ShapeFactory


def findIndexOfFirstObject(list, type):
    first_index = None
    for i in range(len(list)):
        if isinstance(list[i], type):
            first_index = i
    if first_index is None:
        raise ShapeException('findIndexOfLastObject({}, {}) failed to find object in list'.format(list, type))
    return first_index

def findEnd(list, index):
    begin_count = 1
    for i in range(index, len(list)):
        if list[i] == 'begin': begin_count += 1
        elif list[i] == 'end':
            begin_count -= 1
            if begin_count == 0: return i
    raise ShapeException('No matching end found for list<{}> index<{}>'.format(list, index))

class ShapeIO:
    def loadShape(self, string=None, file=None):
        if string is None and file is None:
            raise ShapeException("Expected either a string or file for loadShape")
        if file:
            with open(file, "r") as myfile:
                string = myfile.readlines()
        return self.parse(string)

    def parse(self, string):
        parsed_string = string.strip().split(",")
        shape_tree = self.parseShapeTree(parsed_string)
        shape = self.buildShapes(shape_tree)
        print(shape)
        return shape

    def parseShapeTree(self, parsed_string):
        shape_tree = [parsed_string.pop(0)]
        while len(parsed_string) > 0:
            try:
                shape_tree.append(Point(float(parsed_string[0]), float(parsed_string[1])))
                parsed_string = parsed_string[2:]
            except ValueError: # Not a number, ie shapename or begin/end composite
                shape_tree.append(parsed_string.pop(0))

        return shape_tree

    def buildShapes(self, shape_tree):
        # sample input trees
        # ['composite',0,0,'begin','triangle',1,1,2,2,4,4,'composite',0,0,'begin','rectangle',1,1,2,2,3,3,4,4,'end','end']
        # ['triangle',1,1,2,2,4,4]
        for value in shape_tree: print(value)
        print('-----')
        shapes = [shape_tree[0]]
        i = 1
        while i < len(shape_tree):
            if shape_tree[i] == 'begin':
                begin = i+1
                end = findEnd(shape_tree, i+begin)
                sub_list = shape_tree[begin:end]
                shapes.append(self.buildShapes(sub_list))
                i = end
            elif isinstance(shape_tree[i], str):
                begin = i
                end = findIndexOfFirstObject(shape_tree, str) + 1
                sub_list = shape_tree[begin:end]
                shapes.append(self.buildShapes(sub_list))
                i = end - 1
            else: # it's a point
                shapes.append(shape_tree[i])
            i += 1
        return ShapeFactory.build(shapes.pop(0), *shapes)

    def saveShape(self, shape, file=None):
        string = shape.toString()
        if file: print(string, file=file)
        return string
