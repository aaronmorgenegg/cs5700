#!/usr/bin/env python3

import unittest

from shapes.point import Point
from shapes.shape_exception import ShapeException


class TestPoint(unittest.TestCase):
    def testValidConstruction(self):
        p1 = Point(1, 2)
        self.assertEqual(1, p1.x)
        self.assertEqual(2, p1.y)

        p2 = Point(1.111, 2.222)
        self.assertEqual(1.111, p2.x)
        self.assertEqual(2.222, p2.y)

    def testInvalidConstruction(self):
        self.assertRaises(ShapeException, Point, 1, float('inf'))
        self.assertRaises(ShapeException, Point, 1, float('-inf'))
        self.assertRaises(ShapeException, Point, 1, None)
        self.assertRaises(ShapeException, Point, 1, "2")
        self.assertRaises(ShapeException, Point, float('inf'), 1)
        self.assertRaises(ShapeException, Point, float('-inf'), 1)
        self.assertRaises(ShapeException, Point, None, 1)
        self.assertRaises(ShapeException, Point, "2", 1)
        

