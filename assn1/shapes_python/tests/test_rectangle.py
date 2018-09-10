#!/usr/bin/env python3

import unittest

from shapes.line import Line
from shapes.point import Point
from shapes.rectangle import Rectangle
from shapes.shape_exception import ShapeException


class TestRectangle(unittest.TestCase):
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

    # def testMove(self):
    #     t1 = Triangle(1, 2, 5, 1, 3, 3)
    #
    #     t1.move(3, 4)
    #     self.assertEqual(4, t1.point1.x)
    #     self.assertEqual(6, t1.point1.y)
    #     self.assertEqual(8, t1.point2.x)
    #     self.assertEqual(5, t1.point2.y)
    #     self.assertEqual(6, t1.point3.x)
    #     self.assertEqual(7, t1.point3.y)
    #
    #     t1.move(.4321, .7654)
    #     self.assertEqual(4.4321, t1.point1.x)
    #     self.assertEqual(6.7654, t1.point1.y)
    #     self.assertEqual(8.4321, t1.point2.x)
    #     self.assertEqual(5.7654, t1.point2.y)
    #     self.assertEqual(6.4321, t1.point3.x)
    #     self.assertEqual(7.7654, t1.point3.y)
    #
    #     t1.move(-.4321, -.7654)
    #     self.assertEqual(4, t1.point1.x)
    #     self.assertEqual(6, t1.point1.y)
    #     self.assertEqual(8, t1.point2.x)
    #     self.assertEqual(5, t1.point2.y)
    #     self.assertEqual(6, t1.point3.x)
    #     self.assertEqual(7, t1.point3.y)
    #
    # def testComputeArea(self):
    #     t1 = Triangle(1, 1, 2, 1, 1, 2)
    #     self.assertAlmostEqual(.5, t1.computeArea(), places=4)
    #
    #     t2 = Triangle(1, 2, 5, 1, 3, 3)
    #     self.assertAlmostEqual(3, t2.computeArea(), places=4)
    #
    #     t3 = Triangle(-3, 3, 2, 4, 3, -1)
    #     self.assertAlmostEqual(13, t3.computeArea(), places=4)
