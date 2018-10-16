#!/usr/bin/env python3

import unittest

from shapes.image import Image
from shapes.point import Point
from shapes.shape_exception import ShapeException
from shapes.shape_factory import ShapeFactory


class TestImage(unittest.TestCase):
    def testValidateImage(self):
        i1 = ShapeFactory.build("image", Point(1, 1), Point(4, 1), Point(4, 3), Point(1, 3), "images/red_eyed_tree_frog.png")
        Image.validateImage(i1, "Image unexpectedly invalid")

        self.assertRaises(ShapeException, Image.validateImage, "(1, 1, 4, 1, 4, 3, 1, 3, images/red_eyed_tree_frog.png)",
                          "String \'(1, 1, 4, 1, 4, 3, 1, 3, images/red_eyed_tree_frog.png)\' is not a valid embedded image")
        self.assertRaises(ShapeException, Image.validateImage, Point(1, 1), "Point is not a valid embedded image")

    def testValidConstruction(self):
        p1 = Point(1, 3)
        p2 = Point(5, 3)
        p3 = Point(5, 1)
        p4 = Point(1, 1)
        s1 = "images/red_eyed_tree_frog.png"
        i1 = ShapeFactory.build("image", p1, p2, p3, p4, s1)

        self.assertEqual(p1, i1.point1)
        self.assertEqual(p2, i1.point2)
        self.assertEqual(s1, i1.source)

    def testInvalidConstruction(self):
        p1 = Point(1, 3)
        p2 = Point(5, 3)
        p3 = Point(5, 1)
        p4 = Point(1, 1)
        s1 = "images/red_eyed_tree_frog.png"
        self.assertRaises(ShapeException, ShapeFactory.build, "image", p1, p1, p4, p4, s1)

        s2 = "images/red_eyed_tree_frog.txt"
        self.assertRaises(ShapeException, ShapeFactory.build, "image", p1, p2, p3, p4, s2)

    def testLoadSource(self):
        pass # TODO
