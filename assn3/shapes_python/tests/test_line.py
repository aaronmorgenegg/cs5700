#!/usr/bin/env python3

import unittest

from shapes.line import Line
from shapes.point import Point
from shapes.shape_exception import ShapeException


class TestLine(unittest.TestCase):
    def testValidateLine(self):
        l1 = Line(Point(1, 1), Point(-1, -5))
        Line.validateLine(l1, "Line unexpectedly invalid")

        self.assertRaises(ShapeException, Line.validateLine, "(1, 1, -1, -5)",
                          "String \'(1, 1, -1, -5)\' is not a valid line")
        self.assertRaises(ShapeException, Line.validateLine, Point(1, 1), "Point is not a valid line")

    def testValidConstruction(self):
        p1 = Point(1, 2)
        p2 = Point(4, 10)
        l1 = Line(p1, p2)

        self.assertEqual(p1, l1.point1)
        self.assertEqual(p2, l1.point2)

        p3 = Point(1.4, 2.5)
        p4 = Point(4.6, 10.7)
        l2 = Line(p3, p4)

        self.assertEqual(p3, l2.point1)
        self.assertEqual(p4, l2.point2)

        l3 = Line(Point(1, 3.33), Point(4.444, 5.5555))
        self.assertEqual(1, l3.point1.x)
        self.assertEqual(3.33, l3.point1.y)
        self.assertEqual(4.444, l3.point2.x)
        self.assertEqual(5.5555, l3.point2.y)

    def testInvalidConstruction(self):
        p1 = Point(1, 2)
        p2 = Point(4, 10)

        self.assertRaises(ShapeException, Line, Point(float('inf'), 2), Point(3, 4))
        self.assertRaises(ShapeException, Line, Point(1, float('inf')), Point(3, 4))
        self.assertRaises(ShapeException, Line, Point(1, 2), Point(float('inf'), 4))
        self.assertRaises(ShapeException, Line, Point(1, 2), Point(3, float('inf')))
        self.assertRaises(ShapeException, Line, p1, p1)
        self.assertRaises(ShapeException, Line, Point(1, 2), Point(1, 2))

    def testMove(self):
        l1 = Line(Point(1, 2), Point(4, 10))

        l1.move(3, 4)
        self.assertEqual(4, l1.point1.x)
        self.assertEqual(6, l1.point1.y)
        self.assertEqual(7, l1.point2.x)
        self.assertEqual(14, l1.point2.y)

        l1.move(.4321, .7654)
        self.assertEqual(4.4321, l1.point1.x)
        self.assertEqual(6.7654, l1.point1.y)
        self.assertEqual(7.4321, l1.point2.x)
        self.assertEqual(14.7654, l1.point2.y)

        l1.move(-.4321, -.7654)
        self.assertEqual(4, l1.point1.x)
        self.assertEqual(6, l1.point1.y)
        self.assertEqual(7, l1.point2.x)
        self.assertEqual(14, l1.point2.y)

    def testComputeLength(self):
        l1 = Line(Point(1, 2), Point(4, 10))
        self.assertAlmostEqual(8.544, l1.computeLength(), places=3)

        l2 = Line(Point(1, 2), Point(1, 3))
        self.assertAlmostEqual(1, l2.computeLength(), places=3)

        l3 = Line(Point(3, -2), Point(-4, 10))
        self.assertAlmostEqual(13.892, l3.computeLength(), places=3)

    def testComputeSlope(self):
        l1 = Line(Point(2, 2), Point(4, 10))
        self.assertAlmostEqual(4, l1.computeSlope(), places=3)

        l2 = Line(Point(2, 2), Point(10, 4))
        self.assertAlmostEqual(.25, l2.computeSlope(), places=3)

        l3 = Line(Point(2, 2), Point(4, 2))
        self.assertAlmostEqual(0, l3.computeSlope(), places=3)

        l4 = Line(Point(2, 2), Point(2, 4))
        self.assertAlmostEqual(float('inf'), l4.computeSlope(), places=3)

        l5 = Line(Point(2, 4), Point(2, 2))
        self.assertAlmostEqual(float('-inf'), l5.computeSlope(), places=3)

