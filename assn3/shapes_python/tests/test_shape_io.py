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
