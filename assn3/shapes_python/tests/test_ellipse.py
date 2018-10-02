#!/usr/bin/env python3

import unittest

from shapes.point import Point
from shapes.ellipse import Ellipse
from shapes.shape_exception import ShapeException


class TestEllipse(unittest.TestCase):
    def testValidConstruction(self):
        p1 = Point(0, 0)
        p2 = Point(2, 0)
        p3 = Point(0, 1)
        p4 = Point(3, 0)
        p5 = Point(0, 2)
        e1 = Ellipse(p1, p2, p3, p4, p5)

        self.assertEqual(p1, e1.center)
        self.assertEqual(p2, e1.focus1)
        self.assertEqual(p3, e1.focus2)
        self.assertEqual(p4, e1.edge1)
        self.assertEqual(p5, e1.edge2)

        e2 = Ellipse(1, 1, 4, 4, -2, 4, 6, 6, -2, 4)
        self.assertEqual(1, e2.center.x)
        self.assertEqual(1, e2.center.y)
        self.assertEqual(4, e2.focus1.x)
        self.assertEqual(4, e2.focus1.y)
        self.assertEqual(-2, e2.focus2.x)
        self.assertEqual(4, e2.focus2.y)
        self.assertEqual(6, e2.edge1.x)
        self.assertEqual(6, e2.edge1.y)
        self.assertEqual(-2, e2.edge2.x)
        self.assertEqual(4, e2.edge2.y)

    def testInvalidConstruction(self):
        p1 = Point(0, 0)
        p2 = Point(2, 0)
        p3 = Point(1, 1)
        p4 = Point(3, 0)
        p5 = Point(2, 2)
        self.assertRaises(ShapeException, Ellipse, p1, p2, p3, p4, p5)

        p1 = Point(0, 0)
        p2 = Point(0, 0)
        p3 = Point(0, 0)
        p4 = Point(0, 0)
        p5 = Point(0, 0)
        self.assertRaises(ShapeException, Ellipse, p1, p2, p3, p4, p5)

    def testMove(self):
        e1 = Ellipse(1, 1, 4, 4, -2, 4, 6, 6, -2, 4)

        e1.move(3, 4)
        self.assertAlmostEqual(4, e1.center.x)
        self.assertAlmostEqual(5, e1.center.y)
        self.assertAlmostEqual(7, e1.focus1.x)
        self.assertAlmostEqual(8, e1.focus1.y)
        self.assertAlmostEqual(1, e1.focus2.x)
        self.assertAlmostEqual(8, e1.focus2.y)
        self.assertAlmostEqual(9, e1.edge1.x)
        self.assertAlmostEqual(10, e1.edge1.y)
        self.assertAlmostEqual(1, e1.edge2.x)
        self.assertAlmostEqual(8, e1.edge2.y)

        e1.move(-.234, -1.987)
        self.assertAlmostEqual(3.766, e1.center.x)
        self.assertAlmostEqual(3.013, e1.center.y)
        self.assertAlmostEqual(6.766, e1.focus1.x)
        self.assertAlmostEqual(6.013, e1.focus1.y)
        self.assertAlmostEqual(0.766, e1.focus2.x)
        self.assertAlmostEqual(6.013, e1.focus2.y)
        self.assertAlmostEqual(8.766, e1.edge1.x)
        self.assertAlmostEqual(8.013, e1.edge1.y)
        self.assertAlmostEqual(.766, e1.edge2.x)
        self.assertAlmostEqual(6.013, e1.edge2.y)

        e1.move(.234, 1.987)
        self.assertAlmostEqual(4, e1.center.x)
        self.assertAlmostEqual(5, e1.center.y)
        self.assertAlmostEqual(7, e1.focus1.x)
        self.assertAlmostEqual(8, e1.focus1.y)
        self.assertAlmostEqual(1, e1.focus2.x)
        self.assertAlmostEqual(8, e1.focus2.y)
        self.assertAlmostEqual(9, e1.edge1.x)
        self.assertAlmostEqual(10, e1.edge1.y)
        self.assertAlmostEqual(1, e1.edge2.x)
        self.assertAlmostEqual(8, e1.edge2.y)

    def testComputeArea(self):
        e1 = Ellipse(0, 0, 1, 0, 0, 1, 2, 0, 0, 2)

        self.assertAlmostEqual(12.566, e1.computeArea(), places=3)

        e2 = Ellipse(1, 1, 4, 4, -2, 4, 6, 6, -2, 4)

        self.assertAlmostEqual(94.248, e2.computeArea(), places=3)

    def testScale(self):
        e1 = Ellipse(0, 0, 1, 0, 0, 1, 2, 0, 0, 2)

        e1.scale(2)
        self.assertAlmostEqual(0, e1.center.x)
        self.assertAlmostEqual(0, e1.center.y)
        self.assertAlmostEqual(2, e1.focus1.x)
        self.assertAlmostEqual(0, e1.focus1.y)
        self.assertAlmostEqual(0, e1.focus2.x)
        self.assertAlmostEqual(2, e1.focus2.y)

        e2 = Ellipse(1, 1, 4, 4, -2, 4, 6, 6, -2, 4)

        e2.scale(1/3)
        self.assertAlmostEqual(1, e2.center.x)
        self.assertAlmostEqual(1, e2.center.y)
        self.assertAlmostEqual(2, e2.focus1.x)
        self.assertAlmostEqual(2, e2.focus1.y)
        self.assertAlmostEqual(0, e2.focus2.x)
        self.assertAlmostEqual(2, e2.focus2.y)


