#!/usr/bin/env python3

import unittest

from shapes.line import Line
from shapes.point import Point
from shapes.rectangle import Rectangle
from shapes.shape_exception import ShapeException
from shapes.square import Square


class TestRectangle(unittest.TestCase):
    def testValidConstruction(self):
        p1 = Point(1, 3)
        p2 = Point(5, 3)
        p3 = Point(5, -1)
        p4 = Point(1, -1)
        s1 = Square(p1, p2, p3, p4)

        self.assertEqual(p1, s1.point1)
        self.assertEqual(p2, s1.point2)
        self.assertEqual(p3, s1.point3)
        self.assertEqual(p4, s1.point4)
        self.assertTrue(s1.line1.computeLength() == s1.line2.computeLength() ==
                        s1.line3.computeLength() == s1.line4.computeLength())

        l1 = Line(-3, 1, 1, 1)
        l2 = Line(1, 1, 1, -3)
        l3 = Line(1, -3, -3, -3)
        l4 = Line(-3, -3, -3, 1)
        s2 = Square(l1, l2, l3, l4)

        self.assertEqual(l1, s2.line1)
        self.assertEqual(l2, s2.line2)
        self.assertEqual(l3, s2.line3)
        self.assertEqual(l4, s2.line4)
        self.assertTrue(s2.line1.computeLength() == s2.line2.computeLength() ==
                        s2.line3.computeLength() == s2.line4.computeLength())

        s3 = Square(-.8, .4, 1.2, 2.4, 3.2, .4, 1.2, -1.6)
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
        r1 = Rectangle(p1, p2, p3, p4)
        self.assertRaises(ShapeException, Square, p1, p2, p3, p4)

        l1 = Line(-3, 1, 1, 1)
        l2 = Line(1, 1, 1, -3)
        l3 = Line(1, -3, -3, -3)
        l4 = Line(-3, -3, -3, 2)
        self.assertRaises(ShapeException, Square, l1, l2, l3, l4)

        self.assertRaises(ShapeException, Square, -1, 0, 0, 2, 1, 0, 0, -2)
