#!/usr/bin/env python3

import unittest

from shapes.line import Line
from shapes.point import Point
from shapes.shape_exception import ShapeException
from shapes.shape_factory import ShapeFactory
from shapes.triangle import Triangle


class TestTriangle(unittest.TestCase):
    def testValidateTriangle(self):
        t1 = ShapeFactory.build("triangle", Point(1, 1), Point(-1, -5), Point(-3, -2))
        Triangle.validateTriangle(t1, "Triangle unexpectedly invalid")

        self.assertRaises(ShapeException, Triangle.validateTriangle, "(1, 1, -1, -5, -3, -2)",
                          "String \'(1, 1, -1, -5, -3, -2)\' is not a valid triangle")
        self.assertRaises(ShapeException, Triangle.validateTriangle, Point(1, 1), "Point is not a valid triangle")

    def testValidConstruction(self):
        p1 = Point(1, 2)
        p2 = Point(1, 1)
        p3 = Point(2, 1)
        t1 = ShapeFactory.build("triangle", p1, p2, p3)

        self.assertEqual(p1, t1.point1)
        self.assertEqual(p2, t1.point2)
        self.assertEqual(p3, t1.point3)

        l1 = Line(Point(4.33, 8), Point(-4, 3.67))
        l2 = Line(Point(-4, 3.67), Point(2.19, -5))
        l3 = Line(Point(2.19, -5), Point(4.33, 8))
        t2 = ShapeFactory.build("triangle", l1.point1, l2.point1, l3.point1)

        self.assertEqual(l1, t2.line1)
        self.assertEqual(l2, t2.line2)
        self.assertEqual(l3, t2.line3)

        t3 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))
        self.assertEqual(1, t3.point1.x)
        self.assertEqual(2, t3.point1.y)
        self.assertEqual(5, t3.point2.x)
        self.assertEqual(1, t3.point2.y)
        self.assertEqual(3, t3.point3.x)
        self.assertEqual(3, t3.point3.y)

    def testInvalidConstruction(self):
        p1 = Point(1, 2)
        p2 = Point(1, 1)
        p3 = Point(1, 3)
        self.assertRaises(ShapeException, ShapeFactory.build, "triangle", p1, p2, p3)

        l4 = Line(Point(1, 1), Point(1, 4))
        l5 = Line(Point(2, 1), Point(2, 5))
        l6 = Line(Point(3, 1), Point(3, 6))
        self.assertRaises(ShapeException, ShapeFactory.build, "triangle", l4.point1, l5.point1, l6.point1)

    def testMove(self):
        t1 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))

        t1.move(3, 4)
        self.assertEqual(4, t1.point1.x)
        self.assertEqual(6, t1.point1.y)
        self.assertEqual(8, t1.point2.x)
        self.assertEqual(5, t1.point2.y)
        self.assertEqual(6, t1.point3.x)
        self.assertEqual(7, t1.point3.y)

        t1.move(.4321, .7654)
        self.assertEqual(4.4321, t1.point1.x)
        self.assertEqual(6.7654, t1.point1.y)
        self.assertEqual(8.4321, t1.point2.x)
        self.assertEqual(5.7654, t1.point2.y)
        self.assertEqual(6.4321, t1.point3.x)
        self.assertEqual(7.7654, t1.point3.y)

        t1.move(-.4321, -.7654)
        self.assertEqual(4, t1.point1.x)
        self.assertEqual(6, t1.point1.y)
        self.assertEqual(8, t1.point2.x)
        self.assertEqual(5, t1.point2.y)
        self.assertEqual(6, t1.point3.x)
        self.assertEqual(7, t1.point3.y)

    def testComputeArea(self):
        t1 = ShapeFactory.build("triangle", Point(1, 1), Point(2, 1), Point(1, 2))
        self.assertAlmostEqual(.5, t1.computeArea(), places=4)

        t2 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))
        self.assertAlmostEqual(3, t2.computeArea(), places=4)

        t3 = ShapeFactory.build("triangle", Point(-3, 3), Point(2, 4), Point(3, -1))
        self.assertAlmostEqual(13, t3.computeArea(), places=4)
