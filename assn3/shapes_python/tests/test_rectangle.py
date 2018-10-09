#!/usr/bin/env python3

import unittest

from shapes.line import Line
from shapes.point import Point
from shapes.rectangle import Rectangle
from shapes.shape_exception import ShapeException


class TestRectangle(unittest.TestCase):
    def testValidateRectangle(self):
        r1 = Rectangle(Point(1, 1), Point(4, 1), Point(4, 3), Point(1, 3))
        Rectangle.validateRectangle(r1, "Rectangle unexpectedly invalid")

        self.assertRaises(ShapeException, Rectangle.validateRectangle, "(1, 1, 4, 1, 4, 3, 1, 3)",
                          "String \'(1, 1, 4, 1, 4, 3, 4, 3)\' is not a valid rectangle")
        self.assertRaises(ShapeException, Rectangle.validateRectangle, Point(1, 1), "Point is not a valid rectangle")

    def testValidConstruction(self):
        p1 = Point(1, 3)
        p2 = Point(5, 3)
        p3 = Point(5, 1)
        p4 = Point(1, 1)
        r1 = Rectangle(p1, p2, p3, p4)

        self.assertEqual(p1, r1.point1)
        self.assertEqual(p2, r1.point2)
        self.assertEqual(p3, r1.point3)
        self.assertEqual(p4, r1.point4)

        l1 = Line(-3, 1, 1, 1)
        l2 = Line(1, 1, 1, -5)
        l3 = Line(1, -5, -3, -5)
        l4 = Line(-3, -5, -3, 1)
        r2 = Rectangle(l1, l2, l3, l4)

        self.assertEqual(l1, r2.line1)
        self.assertEqual(l2, r2.line2)
        self.assertEqual(l3, r2.line3)
        self.assertEqual(l4, r2.line4)

        r3 = Rectangle(-.8, .4, 0, 2, .8, 1.6, 0, 0)
        self.assertEqual(-.8, r3.point1.x)
        self.assertEqual(.4, r3.point1.y)
        self.assertEqual(0, r3.point2.x)
        self.assertEqual(2, r3.point2.y)
        self.assertEqual(.8, r3.point3.x)
        self.assertEqual(1.6, r3.point3.y)
        self.assertEqual(0, r3.point4.x)
        self.assertEqual(0, r3.point4.y)

    def testInvalidConstruction(self):
        p1 = Point(1, 3)
        p2 = Point(5, 3)
        p3 = Point(5, 1)
        p4 = Point(1, -1)
        self.assertRaises(ShapeException, Rectangle, p1, p2, p3, p4)

        l1 = Line(-3, 1, 4, 1)
        l2 = Line(1, 1, 1, -5)
        l3 = Line(1, -5, -3, -5)
        l4 = Line(-3, -5, -3, 1)
        self.assertRaises(ShapeException, Rectangle, l1, l2, l3, l4)

        self.assertRaises(ShapeException, Rectangle, -1, 0, 0, 2, 1, 1, 0, -1)

    def testMove(self):
        r1 = Rectangle(-.8, .4, 0, 2, .8, 1.6, 0, 0)

        r1.move(3, 4)
        self.assertAlmostEqual(2.2, r1.point1.x)
        self.assertAlmostEqual(4.4, r1.point1.y)
        self.assertAlmostEqual(3, r1.point2.x)
        self.assertAlmostEqual(6, r1.point2.y)
        self.assertAlmostEqual(3.8, r1.point3.x)
        self.assertAlmostEqual(5.6, r1.point3.y)
        self.assertAlmostEqual(3, r1.point4.x)
        self.assertAlmostEqual(4, r1.point4.y)

        r1.move(-.234, -1.987)
        self.assertAlmostEqual(1.966, r1.point1.x)
        self.assertAlmostEqual(2.413, r1.point1.y)
        self.assertAlmostEqual(2.766, r1.point2.x)
        self.assertAlmostEqual(4.013, r1.point2.y)
        self.assertAlmostEqual(3.566, r1.point3.x)
        self.assertAlmostEqual(3.613, r1.point3.y)
        self.assertAlmostEqual(2.766, r1.point4.x)
        self.assertAlmostEqual(2.013, r1.point4.y)

        r1.move(.234, 1.987)
        self.assertAlmostEqual(2.2, r1.point1.x)
        self.assertAlmostEqual(4.4, r1.point1.y)
        self.assertAlmostEqual(3, r1.point2.x)
        self.assertAlmostEqual(6, r1.point2.y)
        self.assertAlmostEqual(3.8, r1.point3.x)
        self.assertAlmostEqual(5.6, r1.point3.y)
        self.assertAlmostEqual(3, r1.point4.x)
        self.assertAlmostEqual(4, r1.point4.y)

    def testComputeWidth(self):
        r1 = Rectangle(0, 1, 1, 1, 1, 0, 0, 0)
        self.assertAlmostEqual(1, r1.computeWidth(), places=4)

        r2 = Rectangle(-2, 2, 3, 2, 3, 0, -2, 0)
        self.assertAlmostEqual(5, r2.computeWidth(), places=4)

        r3 = Rectangle(-.8, .4, 0, 2, .8, 1.6, 0, 0)
        self.assertAlmostEqual(1.7889, r3.computeWidth(), places=4)

    def testComputeHeight(self):
        r1 = Rectangle(0, 1, 1, 1, 1, 0, 0, 0)
        self.assertAlmostEqual(1, r1.computeHeight(), places=4)

        r2 = Rectangle(-2, 2, 3, 2, 3, 0, -2, 0)
        self.assertAlmostEqual(2, r2.computeHeight(), places=4)

        r3 = Rectangle(-.8, .4, 0, 2, .8, 1.6, 0, 0)
        self.assertAlmostEqual(.8944, r3.computeHeight(), places=4)

    def testComputeArea(self):
        r1 = Rectangle(0, 1, 1, 1, 1, 0, 0, 0)
        self.assertAlmostEqual(1, r1.computeArea(), places=4)

        r2 = Rectangle(-2, 2, 3, 2, 3, 0, -2, 0)
        self.assertAlmostEqual(10, r2.computeArea(), places=4)

        r3 = Rectangle(-.8, .4, 0, 2, .8, 1.6, 0, 0)
        self.assertAlmostEqual(1.6, r3.computeArea(), places=4)
