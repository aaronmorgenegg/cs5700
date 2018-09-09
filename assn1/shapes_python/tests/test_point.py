#!/usr/bin/env python3

import unittest

from shapes.point import Point


class TestPoint(unittest.TestCase):
    def testValidConstruction(self):
        p1 = Point(1, 2)
        self.assertEqual(1, p1.x)
        self.assertEqual(2, p1.y)

        p2 = Point(1.111, 2.222)
        self.assertEqual(1.111, p2.x)
        self.assertEqual(2.222, p2.y)
        

