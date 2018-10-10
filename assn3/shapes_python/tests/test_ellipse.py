#!/usr/bin/env python3

import unittest

from shapes.point import Point
from shapes.ellipse import Ellipse
from shapes.shape_exception import ShapeException
from shapes.shape_factory import ShapeFactory


class TestEllipse(unittest.TestCase):
    def testValidateEllipse(self):
        e1 = ShapeFactory.build("ellipse", Point(0, 0), Point(3, 0), Point(0, 2))
        Ellipse.validateEllipse(e1, "Ellipse unexpectedly invalid")

        self.assertRaises(ShapeException, Ellipse.validateEllipse, "(0, 0, 3, 0, 0, 2)",
                          "String \'(0, 0, 3, 0, 0, 2)\' is not a valid ellipse")
        self.assertRaises(ShapeException, Ellipse.validateEllipse, Point(1, 1), "Point is not a valid ellipse")

    def testValidConstruction(self):
        p1 = Point(0, 0)
        p2 = Point(3, 0)
        p3 = Point(0, 2)
        e1 = ShapeFactory.build("ellipse", p1, p2, p3)

        self.assertEqual(p1, e1.center)
        self.assertEqual(p2, e1.point1)
        self.assertEqual(p3, e1.point2)

        e2 = ShapeFactory.build("ellipse", Point(1, 1), Point(6, 6), Point(-2, 4))
        self.assertEqual(1, e2.center.x)
        self.assertEqual(1, e2.center.y)
        self.assertEqual(6, e2.point1.x)
        self.assertEqual(6, e2.point1.y)
        self.assertEqual(-2, e2.point2.x)
        self.assertEqual(4, e2.point2.y)

    def testInvalidConstruction(self):
        p1 = Point(0, 0)
        p2 = Point(3, 0)
        p3 = Point(2, 2)
        self.assertRaises(ShapeException, ShapeFactory.build, "ellipse", p1, p2, p3)

        p1 = Point(0, 0)
        p2 = Point(0, 0)
        p3 = Point(0, 0)
        self.assertRaises(ShapeException, ShapeFactory.build, "ellipse", p1, p2, p3)

    def testMove(self):
        e1 = ShapeFactory.build("ellipse", Point(1, 1), Point(6, 6), Point(-2, 4))

        e1.move(3, 4)
        self.assertAlmostEqual(4, e1.center.x)
        self.assertAlmostEqual(5, e1.center.y)
        self.assertAlmostEqual(9, e1.point1.x)
        self.assertAlmostEqual(10, e1.point1.y)
        self.assertAlmostEqual(1, e1.point2.x)
        self.assertAlmostEqual(8, e1.point2.y)

        e1.move(-.234, -1.987)
        self.assertAlmostEqual(3.766, e1.center.x)
        self.assertAlmostEqual(3.013, e1.center.y)
        self.assertAlmostEqual(8.766, e1.point1.x)
        self.assertAlmostEqual(8.013, e1.point1.y)
        self.assertAlmostEqual(.766, e1.point2.x)
        self.assertAlmostEqual(6.013, e1.point2.y)

        e1.move(.234, 1.987)
        self.assertAlmostEqual(4, e1.center.x)
        self.assertAlmostEqual(5, e1.center.y)
        self.assertAlmostEqual(9, e1.point1.x)
        self.assertAlmostEqual(10, e1.point1.y)
        self.assertAlmostEqual(1, e1.point2.x)
        self.assertAlmostEqual(8, e1.point2.y)

    def testComputeArea(self):
        e1 = ShapeFactory.build("ellipse", Point(0, 0), Point(2, 0), Point(0, 2))

        self.assertAlmostEqual(12.566, e1.computeArea(), places=3)

        e2 = ShapeFactory.build("ellipse", Point(1, 1), Point(6, 6), Point(-2, 4))

        self.assertAlmostEqual(94.248, e2.computeArea(), places=3)

    def testScale(self):
        e1 = ShapeFactory.build("ellipse", Point(0, 0), Point(2, 0), Point(0, 2))

        e1.scale(2)
        self.assertAlmostEqual(0, e1.center.x)
        self.assertAlmostEqual(0, e1.center.y)
        self.assertAlmostEqual(4, e1.point1.x)
        self.assertAlmostEqual(0, e1.point1.y)
        self.assertAlmostEqual(0, e1.point2.x)
        self.assertAlmostEqual(4, e1.point2.y)

        e2 = ShapeFactory.build("ellipse", Point(1, 1), Point(4, 4), Point(-2, 4))

        e2.scale(1/3)
        self.assertAlmostEqual(1, e2.center.x)
        self.assertAlmostEqual(1, e2.center.y)
        self.assertAlmostEqual(2, e2.point1.x)
        self.assertAlmostEqual(2, e2.point1.y)
        self.assertAlmostEqual(0, e2.point2.x)
        self.assertAlmostEqual(2, e2.point2.y)


