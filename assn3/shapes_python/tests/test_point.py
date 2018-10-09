#!/usr/bin/env python3

import unittest

from shapes.point import Point
from shapes.shape_exception import ShapeException


class TestPoint(unittest.TestCase):
    def testValidatePoint(self):
        p1 = Point(1, 1)
        Point.validatePoint(p1, "Point unexpectedly invalid")

        self.assertRaises(ShapeException, Point.validatePoint, "(1, 1)",
                          "String \'(1, 1)\' is not a valid point")

    def testValidConstruction(self):
        p1 = Point(1, 2)
        self.assertEqual(1, p1.x)
        self.assertEqual(2, p1.y)

        p2 = Point(1.111, 2.222)
        self.assertEqual(1.111, p2.x)
        self.assertEqual(2.222, p2.y)

    def testInvalidConstruction(self):
        self.assertRaises(ShapeException, Point)
        self.assertRaises(ShapeException, Point, 1, float('inf'))
        self.assertRaises(ShapeException, Point, 1, float('-inf'))
        self.assertRaises(ShapeException, Point, 1, None)
        self.assertRaises(ShapeException, Point, 1, "2")
        self.assertRaises(ShapeException, Point, float('inf'), 1)
        self.assertRaises(ShapeException, Point, float('-inf'), 1)
        self.assertRaises(ShapeException, Point, None, 1)
        self.assertRaises(ShapeException, Point, "2", 1)
        
    def testMoveX(self):
        p1 = Point(1, 2)

        p1.move(10, 0)
        self.assertEqual(p1.x, 11)
        self.assertEqual(p1.y, 2)

        p1.move(.1234, 0)
        self.assertEqual(p1.x, 11.1234)
        self.assertEqual(p1.y, 2)

        p1.move(-20, 0)
        self.assertEqual(p1.x, -8.8766)
        self.assertEqual(p1.y, 2)

        p1.move(0, 0)
        self.assertEqual(p1.x, -8.8766)
        self.assertEqual(p1.y, 2)

        self.assertRaises(ShapeException, p1.move, float('inf'), 0)
        self.assertRaises(ShapeException, p1.move, float('-inf'), 0)
        self.assertRaises(ShapeException, p1.move, None, 0)
        self.assertRaises(ShapeException, p1.move, "2", 0)

    def testMoveY(self):
        p1 = Point(1, 2)

        p1.move(0, 10)
        self.assertEqual(p1.x, 1)
        self.assertEqual(p1.y, 12)

        p1.move(0, .1234)
        self.assertEqual(p1.x, 1)
        self.assertEqual(p1.y, 12.1234)

        p1.move(0, -20)
        self.assertEqual(p1.x, 1)
        self.assertEqual(p1.y, -7.8766)

        p1.move(0, 0)
        self.assertEqual(p1.x, 1)
        self.assertEqual(p1.y, -7.8766)

        self.assertRaises(ShapeException, p1.move, 0, float('inf'))
        self.assertRaises(ShapeException, p1.move, 0, float('-inf'))
        self.assertRaises(ShapeException, p1.move, 0, None)
        self.assertRaises(ShapeException, p1.move, 0, "2")

    def testMove(self):
        p1 = Point(1, 2)

        p1.move(2, 10)
        self.assertEqual(p1.x, 3)
        self.assertEqual(p1.y, 12)

        p1.move(.1234, .5678)
        self.assertEqual(p1.x, 3.1234)
        self.assertEqual(p1.y, 12.5678)

        p1.move(-10, -20)
        self.assertEqual(p1.x, -6.8766)
        self.assertEqual(p1.y, -7.4322)

        p1.move(0, 0)
        self.assertEqual(p1.x, -6.8766)
        self.assertEqual(p1.y, -7.4322)

        self.assertRaises(ShapeException, p1.move, float('inf'), float('inf'))
        self.assertRaises(ShapeException, p1.move, float('-inf'), float('-inf'))
        self.assertRaises(ShapeException, p1.move, None, None)
        self.assertRaises(ShapeException, p1.move, "3", "2")

    def testClone(self):
        p1 = Point(-123.45, -23.45)
        self.assertEqual(-123.45, p1.x)
        self.assertEqual(-23.45, p1.y)

        p2 = p1.copy()
        self.assertFalse(p1 is p2)
        self.assertEqual(p1.x, p2.x)
        self.assertEqual(p1.y, p2.y)

    def testEquality(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        self.assertEqual(p1, p2)
        p2.move(1, 1)
        self.assertNotEqual(p1, p2)
