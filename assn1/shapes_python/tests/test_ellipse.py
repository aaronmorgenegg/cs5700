#!/usr/bin/env python3

import unittest

from shapes.point import Point
from shapes.ellipse import Ellipse
from shapes.shape_exception import ShapeException


class TestRectangle(unittest.TestCase):
    def testValidConstruction(self):
        p1 = Point(0, 0)
        p2 = Point(2, 0)
        p3 = Point(0, 1)
        e1 = Ellipse(p1, p2, p3)

        self.assertEqual(p1, e1.center)
        self.assertEqual(p2, e1.focus1)
        self.assertEqual(p3, e1.focus2)

        e2 = Ellipse(1, 1, 4, 4, -1, 3)
        self.assertEqual(1, e2.center.x)
        self.assertEqual(1, e2.center.y)
        self.assertEqual(4, e2.focus1.x)
        self.assertEqual(4, e2.focus1.y)
        self.assertEqual(-1, e2.focus2.x)
        self.assertEqual(3, e2.focus2.y)

    def testInvalidConstruction(self):
        p1 = Point(0, 0)
        p2 = Point(2, 0)
        p3 = Point(1, 1)
        self.assertRaises(ShapeException, Ellipse, p1, p2, p3)

        p1 = Point(0, 0)
        p2 = Point(0, 0)
        p3 = Point(0, 0)
        self.assertRaises(ShapeException, Ellipse, p1, p2, p3)

    def testMove(self):
        e1 = Ellipse(1, 1, 4, 4, -1, 3)

        e1.move(3, 4)
        self.assertAlmostEqual(4, e1.center.x)
        self.assertAlmostEqual(5, e1.center.y)
        self.assertAlmostEqual(7, e1.focus1.x)
        self.assertAlmostEqual(8, e1.focus1.y)
        self.assertAlmostEqual(2, e1.focus2.x)
        self.assertAlmostEqual(7, e1.focus2.y)

        e1.move(-.234, -1.987)
        self.assertAlmostEqual(3.766, e1.center.x)
        self.assertAlmostEqual(3.013, e1.center.y)
        self.assertAlmostEqual(6.766, e1.focus1.x)
        self.assertAlmostEqual(6.013, e1.focus1.y)
        self.assertAlmostEqual(1.766, e1.focus2.x)
        self.assertAlmostEqual(5.013, e1.focus2.y)

        e1.move(.234, 1.987)
        self.assertAlmostEqual(4, e1.center.x)
        self.assertAlmostEqual(5, e1.center.y)
        self.assertAlmostEqual(7, e1.focus1.x)
        self.assertAlmostEqual(8, e1.focus1.y)
        self.assertAlmostEqual(2, e1.focus2.x)
        self.assertAlmostEqual(7, e1.focus2.y)
