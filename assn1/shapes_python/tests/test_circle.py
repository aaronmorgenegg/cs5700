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
        p4 = Point(3, 0)
        p5 = Point(0, 3)
        c1 = Circle(p1, p2, p3, p4, p5)

        self.assertEqual(p1, c1.center)
        self.assertEqual(p2, c1.focus1)
        self.assertEqual(p3, c1.focus2)
        self.assertEqual(p4, c1.edge1)
        self.assertEqual(p5, c1.edge2)

        c2 = Circle(1, 1, 4, 4, -2, 4, 6, 6, -4, 6)
        self.assertEqual(1, c2.center.x)
        self.assertEqual(1, c2.center.y)
        self.assertEqual(4, c2.focus1.x)
        self.assertEqual(4, c2.focus1.y)
        self.assertEqual(-2, c2.focus2.x)
        self.assertEqual(4, c2.focus2.y)
        self.assertEqual(6, c2.edge1.x)
        self.assertEqual(6, c2.edge1.y)
        self.assertEqual(-4, c2.edge2.x)
        self.assertEqual(6, c2.edge2.y)

    def testInvalidConstruction(self):
        p1 = Point(0, 0)
        p2 = Point(2, 0)
        p3 = Point(0, 1)
        p4 = Point(3, 0)
        p5 = Point(0, 2)
        self.assertRaises(ShapeException, Circle, p1, p2, p3, p4, p5)

        p1 = Point(0, 0)
        p2 = Point(0, 0)
        p3 = Point(0, 0)
        p4 = Point(0, 0)
        p5 = Point(0, 0)
        self.assertRaises(ShapeException, Circle, p1, p2, p3, p4, p5)

    def testComputeRadius(self):
        p1 = Point(0, 0)
        p2 = Point(1, 0)
        p3 = Point(0, 1)
        p4 = Point(2, 0)
        p5 = Point(0, 2)
        c1 = Circle(p1, p2, p3, p4, p5)
        self.assertAlmostEqual(2, c1.computeRadius(), places=3)

        c2 = Circle(1, 1, 4, 4, -2, 4, 6, 6, -4, 6)
        self.assertAlmostEqual(7.071, c2.computeRadius(), places=3)

