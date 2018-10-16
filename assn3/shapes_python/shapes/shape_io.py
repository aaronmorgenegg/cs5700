#!/usr/bin/env python3

"""
Handles shape IO

Load and save shapes in a simple scripting format,
either to/from a string, stdin, or a file
"""
from shapes.constants import VALID_IMAGES
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
        return self.parse(string)

    def parse(self, string):
        parsed_string = string.strip().split(",")
        shape_tree = self._parseShapeTree(parsed_string)
        shape_tree = self._buildShapes(shape_tree)
        shape = self._buildComposites(shape_tree)
        return shape

    def _parseShapeTree(self, parsed_string):
        """
        Parses input string into list of arguments

        Also builds points where appropriate
        :param parsed_string: string of saved shape data
        :return: list of arguments, which are either shape names or point objects
        """
        shape_tree = [parsed_string.pop(0)]
        while len(parsed_string) > 0:
            try:
                shape_tree.append(Point(float(parsed_string[0]), float(parsed_string[1])))
                parsed_string = parsed_string[2:]
            except ValueError: # Not a number, ie shapename or begin/end composite
                shape_tree.append(parsed_string.pop(0))

        return shape_tree

    def _buildShapes(self, shape_tree):
        """
        Builds non-composite shapes from a parsed shape_tree


        sample input trees
        ['composite',0,0,'begin','triangle',1,1,2,2,4,4,'composite',0,0,'begin','rectangle',1,1,2,2,3,3,4,4,'end','end']
        ['triangle',1,1,2,2,4,4]

        :param shape_tree: list of arguments of either shape names, or point objects
        :return: list of composite names, or shape objects
        """
        shapes = []
        points = []
        current_shape = None
        i = 0
        while i < len(shape_tree):
            if shape_tree[i] == 'begin' or shape_tree[i] == 'end':
                shapes, current_shape, points = self._buildShape(shapes, current_shape, points)
                shapes.append(shape_tree[i])
            elif shape_tree[i] == 'composite':
                shapes, current_shape, points = self._buildShape(shapes, current_shape, points)
                shapes.append(shape_tree[i])
                shapes.append(shape_tree[i+1])
                i += 1
            elif isinstance(shape_tree[i], str) and shape_tree[i].endswith(VALID_IMAGES):
                points.append(shape_tree[i])
            elif isinstance(shape_tree[i], str):
                shapes, current_shape, points = self._buildShape(shapes, current_shape, points)

                current_shape = shape_tree[i]
            else: # it's a point
                points.append(shape_tree[i])
            i += 1
        shapes, current_shape, points = self._buildShape(shapes, current_shape, points)
        return shapes

    def _buildShape(self, shapes, shape, points):
        if len(points) > 0 and shape is not None:
            shapes.append(ShapeFactory.build(shape, *points))
            return shapes, None, []
        return shapes, shape, points

    def _buildComposites(self, shape_tree):
        """
        Build all of composite shapes in given shape_tree

        Returns a single shape, which may be a composite shape
        :param shape_tree: list of composite identifiers(composite, begin, end),
        composite center points, or shape objects
        :return: shape object (single shape or a composite shape)
        """
        # TODO get this working
        return shape_tree[0]
        # if shape_tree[0] == 'composite':
        #     begin = 2
        #     end = self._findEnd(shape_tree, begin+1)
        #     shape_tree.pop(end)
        #     shape_tree.pop(begin)
        #     name = shape_tree.pop(0)
        #     center = shape_tree.pop(0)
        #     sublist = shape_tree[begin:end]
        #     print(sublist)
        #     if 'composite' in sublist:
        #         self._buildComposites(sublist)
        #
        #     shape_tree[0] = ShapeFactory.build(name, center, *shape_tree)
        # return shape_tree[0]

    def _findEnd(self, list, index):
        begin_count = 1
        for i in range(index, len(list)):
            if list[i] == 'begin':
                begin_count += 1
            elif list[i] == 'end':
                begin_count -= 1
                if begin_count == 0: return i
        raise ShapeException('No matching end found for list<{}> index<{}>'.format(list, index))

    def saveShape(self, shape, file=None):
        string = shape.toString()
        if file: print(string, file=file)
        return string
