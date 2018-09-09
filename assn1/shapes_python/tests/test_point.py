#!/usr/bin/env python3

import unittest

import shapes
from shapes.point import *

class TestPoint(unittest.TestCase):
    def testValidConstruction(self):
        p1 = Point(1, 2)
        self.assertEquals(1, p1.x)
        self.assertEquals(2, p1.y)

        p2 = Point(1.111, 2.222)
        self.assertEquals(1.111, p2.x)
        self.assertEquals(2.222, p2.y)
        

