#!/usr/bin/env python3

import unittest

from shapes.line import Line
from shapes.point import Point
from shapes.rectangle import Rectangle
from shapes.shape_exception import ShapeException
from shapes.shape_factory import ShapeFactory
from shapes.square import Square


class TestRectangle(unittest.TestCase):
    def testValidateSquare(self):
        s1 = ShapeFactory.build("square", Point(1, 1), Point(3, 1), Point(3, 3), Point(1, 3))
        Square.validateSquare(s1, "Square unexpectedly invalid")

        self.assertRaises(ShapeException, Square.validateSquare, "(1, 1, 3, 1, 3, 3, 1, 3)",
                          "String \'(1, 1, 3, 1, 3, 3, 3, 3)\' is not a valid square")
        self.assertRaises(ShapeException, Square.validateSquare, Point(1, 1), "Point is not a valid square")

    def testValidConstruction(self):
        p1 = Point(1, 3)
        p2 = Point(5, 3)
        p3 = Point(5, -1)
        p4 = Point(1, -1)
        s1 = ShapeFactory.build("square", p1, p2, p3, p4)

        self.assertEqual(p1, s1.point1)
        self.assertEqual(p2, s1.point2)
        self.assertEqual(p3, s1.point3)
        self.assertEqual(p4, s1.point4)
        self.assertTrue(s1.line1.computeLength() == s1.line2.computeLength() ==
                        s1.line3.computeLength() == s1.line4.computeLength())

        l1 = Line(Point(-3, 1), Point(1, 1))
        l2 = Line(Point(1, 1), Point(1, -3))
        l3 = Line(Point(1, -3), Point(-3, -3))
        l4 = Line(Point(-3, -3), Point(-3, 1))
        s2 = ShapeFactory.build("square", l1.point1, l2.point1, l3.point1, l4.point1)

        self.assertEqual(l1, s2.line1)
        self.assertEqual(l2, s2.line2)
        self.assertEqual(l3, s2.line3)
        self.assertEqual(l4, s2.line4)
        self.assertTrue(s2.line1.computeLength() == s2.line2.computeLength() ==
                        s2.line3.computeLength() == s2.line4.computeLength())

        s3 = ShapeFactory.build("square", Point(-.8, .4), Point(1.2, 2.4), Point(3.2, .4), Point(1.2, -1.6))
        self.assertEqual(-.8, s3.point1.x)
        self.assertEqual(.4, s3.point1.y)
        self.assertEqual(1.2, s3.point2.x)
        self.assertEqual(2.4, s3.point2.y)
        self.assertEqual(3.2, s3.point3.x)
        self.assertEqual(.4, s3.point3.y)
        self.assertEqual(1.2, s3.point4.x)
        self.assertEqual(-1.6, s3.point4.y)
        self.assertTrue(s3.line1.computeLength() == s3.line2.computeLength() ==
                        s3.line3.computeLength() == s3.line4.computeLength())

    def testInvalidConstruction(self):
        p1 = Point(1, 3)
        p2 = Point(5, 3)
        p3 = Point(5, 1)
        p4 = Point(1, 1)
        r1 = ShapeFactory.build("rectangle", p1, p2, p3, p4)
        self.assertRaises(ShapeException, ShapeFactory.build, "square", p1, p2, p3, p4)

        self.assertRaises(ShapeException, ShapeFactory.build, "square", Point(-1, 0), Point(0, 2), Point(1, 0), Point(0, -2))
