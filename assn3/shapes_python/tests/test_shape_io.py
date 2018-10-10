#!/usr/bin/env python3

import unittest

from shapes.point import Point
from shapes.shape_factory import ShapeFactory
from shapes.shape_io import ShapeIO


class TestShapeIO(unittest.TestCase):
    def testSaveToString(self):
        r1 = ShapeFactory.build("rectangle", Point(1, 1), Point(4, 1), Point(4, 3), Point(1, 3))
        expected = r1.toString()
        testShapeIO = ShapeIO()
        actual = testShapeIO.saveShape(r1)
        self.assertEqual(expected, actual)

    def testLoadFromString(self):
        rectangle = "rectangle,1,1,4,1,4,3,1,3"
        testShapeIO = ShapeIO()
        r1 = testShapeIO.loadShape(string=rectangle)
        self.assertEqual(r1.point1.x, 1)
        self.assertEqual(r1.point1.y, 1)
        self.assertEqual(r1.point2.x, 4)
        self.assertEqual(r1.point2.y, 1)
        self.assertEqual(r1.point3.x, 4)
        self.assertEqual(r1.point3.y, 3)
        self.assertEqual(r1.point4.x, 1)
        self.assertEqual(r1.point4.y, 3)
