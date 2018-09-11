#!/usr/bin/env python3

import unittest

from shapes.circle import Circle
from shapes.point import Point
from shapes.shape_exception import ShapeException


class TestCircle(unittest.TestCase):
    def testValidConstruction(self):
        p1 = Point(0, 0)
        p2 = Point(2, 0)
        p3 = Point(0, 2)
        c1 = Circle(p1, p2, p3)

        self.assertEqual(p1, c1.center)
        self.assertEqual(p2, c1.focus1)
        self.assertEqual(p3, c1.focus2)

        c2 = Circle(1, 1, 4, 4, -2, 4)
        self.assertEqual(1, c2.center.x)
        self.assertEqual(1, c2.center.y)
        self.assertEqual(4, c2.focus1.x)
        self.assertEqual(4, c2.focus1.y)
        self.assertEqual(-2, c2.focus2.x)
        self.assertEqual(4, c2.focus2.y)

    @unittest.skip
    def testInvalidConstruction(self):
        p1 = Point(0, 0)
        p2 = Point(2, 0)
        p3 = Point(0, 1)
        self.assertRaises(ShapeException, Circle, p1, p2, p3)

        p1 = Point(0, 0)
        p2 = Point(0, 0)
        p3 = Point(0, 0)
        self.assertRaises(ShapeException, Circle, p1, p2, p3)

    @unittest.skip
    def testComputeRadius(self):
        p1 = Point(0, 0)
        p2 = Point(2, 0)
        p3 = Point(0, 1)
        c1 = Circle(p1, p2, p3)
        self.assertEqual(2, c1.computeArea())

        c2 = Circle(1, 1, 4, 4, -2, 4)
        self.assertEqual(3, c2.computeRadius())

