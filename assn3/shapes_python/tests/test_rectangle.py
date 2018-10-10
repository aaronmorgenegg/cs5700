#!/usr/bin/env python3

import unittest

from shapes.line import Line
from shapes.point import Point
from shapes.rectangle import Rectangle
from shapes.shape_exception import ShapeException
from shapes.shape_factory import ShapeFactory


class TestRectangle(unittest.TestCase):
    def testValidateRectangle(self):
        r1 = ShapeFactory.build("rectangle", Point(1, 1), Point(4, 1), Point(4, 3), Point(1, 3))
        Rectangle.validateRectangle(r1, "Rectangle unexpectedly invalid")

        self.assertRaises(ShapeException, Rectangle.validateRectangle, "(1, 1, 4, 1, 4, 3, 1, 3)",
                          "String \'(1, 1, 4, 1, 4, 3, 4, 3)\' is not a valid rectangle")
        self.assertRaises(ShapeException, Rectangle.validateRectangle, Point(1, 1), "Point is not a valid rectangle")

    def testValidConstruction(self):
        p1 = Point(1, 3)
        p2 = Point(5, 3)
        p3 = Point(5, 1)
        p4 = Point(1, 1)
        r1 = ShapeFactory.build("rectangle", p1, p2, p3, p4)

        self.assertEqual(p1, r1.point1)
        self.assertEqual(p2, r1.point2)
        self.assertEqual(p3, r1.point3)
        self.assertEqual(p4, r1.point4)

        l1 = Line(Point(-3, 1), Point(1, 1))
        l2 = Line(Point(1, 1), Point(1, -5))
        l3 = Line(Point(1, -5), Point(-3, -5))
        l4 = Line(Point(-3, -5), Point(-3, 1))
        r2 = ShapeFactory.build("rectangle", l1.point1, l2.point1, l3.point1, l4.point1)

        self.assertEqual(l1, r2.line1)
        self.assertEqual(l2, r2.line2)
        self.assertEqual(l3, r2.line3)
        self.assertEqual(l4, r2.line4)

        r3 = ShapeFactory.build("rectangle", Point(-.8, .4), Point(0, 2), Point(.8, 1.6), Point(0, 0))
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
        self.assertRaises(ShapeException, ShapeFactory.build, "rectangle", p1, p2, p3, p4)

        self.assertRaises(ShapeException, ShapeFactory.build, "rectangle", Point(-1, 0), Point(0, 2), Point(1, 1), Point(0, -1))

    def testMove(self):
        r1 = ShapeFactory.build("rectangle", Point(-.8, .4), Point(0, 2), Point(.8, 1.6), Point(0, 0))

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
        r1 = ShapeFactory.build("rectangle", Point(0, 1), Point(1, 1), Point(1, 0), Point(0, 0))
        self.assertAlmostEqual(1, r1.computeWidth(), places=4)

        r2 = ShapeFactory.build("rectangle", Point(-2, 2), Point(3, 2), Point(3, 0), Point(-2, 0))
        self.assertAlmostEqual(5, r2.computeWidth(), places=4)

        r3 = ShapeFactory.build("rectangle", Point(-.8, .4), Point(0, 2), Point(.8, 1.6), Point(0, 0))
        self.assertAlmostEqual(1.7889, r3.computeWidth(), places=4)

    def testComputeHeight(self):
        r1 = ShapeFactory.build("rectangle", Point(0, 1), Point(1, 1), Point(1, 0), Point(0, 0))
        self.assertAlmostEqual(1, r1.computeHeight(), places=4)

        r2 = ShapeFactory.build("rectangle", Point(-2, 2), Point(3, 2), Point(3, 0), Point(-2, 0))
        self.assertAlmostEqual(2, r2.computeHeight(), places=4)

        r3 = ShapeFactory.build("rectangle", Point(-.8, .4), Point(0, 2), Point(.8, 1.6), Point(0, 0))
        self.assertAlmostEqual(.8944, r3.computeHeight(), places=4)

    def testComputeArea(self):
        r1 = ShapeFactory.build("rectangle", Point(0, 1), Point(1, 1), Point(1, 0), Point(0, 0))
        self.assertAlmostEqual(1, r1.computeArea(), places=4)

        r2 = ShapeFactory.build("rectangle", Point(-2, 2), Point(3, 2), Point(3, 0), Point(-2, 0))
        self.assertAlmostEqual(10, r2.computeArea(), places=4)

        r3 = ShapeFactory.build("rectangle", Point(-.8, .4), Point(0, 2), Point(.8, 1.6), Point(0, 0))
        self.assertAlmostEqual(1.6, r3.computeArea(), places=4)
