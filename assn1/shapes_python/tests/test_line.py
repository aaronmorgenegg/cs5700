#!/usr/bin/env python3

import unittest

from shapes.line import Line
from shapes.point import Point


class TestLine(unittest.TestCase):
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

        l3 = Line(1, 3.33, 4.444, 5.5555)
        self.assertEqual(1, l3.point1.x)
        self.assertEqual(3.33, l3.point1.y)
        self.assertEqual(4.444, l3.point2.x)
        self.assertEqual(5.5555, l3.point2.y)

    
