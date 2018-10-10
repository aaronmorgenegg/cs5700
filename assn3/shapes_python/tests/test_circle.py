#!/usr/bin/env python3

import unittest

from shapes.circle import Circle
from shapes.point import Point
from shapes.shape_exception import ShapeException
from shapes.shape_factory import ShapeFactory


class TestCircle(unittest.TestCase):
    def testValidateCircle(self):
        c1 = ShapeFactory.build("circle", Point(0, 0), Point(2, 0), Point(0, 2))
        Circle.validateCircle(c1, "Circle unexpectedly invalid")

        self.assertRaises(ShapeException, Circle.validateCircle, "(0, 0, 2, 0, 0, 2)",
                          "String \'(0, 0, 2, 0, 0, 2)\' is not a valid circle")
        self.assertRaises(ShapeException, Circle.validateCircle, Point(1, 1), "Point is not a valid circle")


    def testValidConstruction(self):
        p1 = Point(0, 0)
        p2 = Point(3, 0)
        p3 = Point(0, 3)
        c1 = ShapeFactory.build("circle", p1, p2, p3)

        self.assertEqual(p1, c1.center)
        self.assertEqual(p2, c1.point1)
        self.assertEqual(p3, c1.point2)

        c2 = ShapeFactory.build("circle", Point(1, 1), Point(6, 6), Point(-4, 6))
        self.assertEqual(1, c2.center.x)
        self.assertEqual(1, c2.center.y)
        self.assertEqual(6, c2.point1.x)
        self.assertEqual(6, c2.point1.y)
        self.assertEqual(-4, c2.point2.x)
        self.assertEqual(6, c2.point2.y)

    def testInvalidConstruction(self):
        p1 = Point(0, 0)
        p2 = Point(3, 0)
        p3 = Point(0, 2)
        self.assertRaises(ShapeException, ShapeFactory.build, "circle", p1, p2, p3)

        p1 = Point(0, 0)
        p2 = Point(0, 0)
        p3 = Point(0, 0)
        self.assertRaises(ShapeException, ShapeFactory.build, "circle", p1, p2, p3)

    def testComputeRadius(self):
        p1 = Point(0, 0)
        p2 = Point(2, 0)
        p3 = Point(0, 2)
        c1 = ShapeFactory.build("circle", p1, p2, p3)
        self.assertAlmostEqual(2, c1.computeRadius(), places=3)

        c2 = ShapeFactory.build("circle", Point(1, 1), Point(6, 6), Point(-4, 6))
        self.assertAlmostEqual(7.071, c2.computeRadius(), places=3)

