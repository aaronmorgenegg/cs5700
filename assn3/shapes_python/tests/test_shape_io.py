#!/usr/bin/env python3

import unittest

from shapes.point import Point
from shapes.shape_factory import ShapeFactory
from shapes.shape_io import ShapeIO


class TestShapeIO(unittest.TestCase):
    def testSaveToString(self):
        r1 = ShapeFactory.build("rectangle", Point(1, 1), Point(4, 1), Point(4, 3), Point(1, 3))
        expected = r1.toString()
        testShapeIO = ShapeIO()
        actual = testShapeIO.saveShape(r1)
        self.assertEqual(expected, actual)

    def testLoadFromString(self):
        rectangle = "rectangle,1,1,4,1,4,3,1,3"
        testShapeIO = ShapeIO()
        r1 = testShapeIO.loadShape(string=rectangle)
        self.assertEqual(r1.point1.x, 1)
        self.assertEqual(r1.point1.y, 1)
        self.assertEqual(r1.point2.x, 4)
        self.assertEqual(r1.point2.y, 1)
        self.assertEqual(r1.point3.x, 4)
        self.assertEqual(r1.point3.y, 3)
        self.assertEqual(r1.point4.x, 1)
        self.assertEqual(r1.point4.y, 3)

    def testSaveComposite(self):
        center = Point(0, 0)
        r1 = ShapeFactory.build("rectangle", Point(1, 1), Point(4, 1), Point(4, 3), Point(1, 3))
        t1 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))
        c1 = ShapeFactory.build("circle", Point(0, 0), Point(2, 0), Point(0, 2))
        e1 = ShapeFactory.build("ellipse", Point(0, 0), Point(3, 0), Point(0, 2))
        cm1 = ShapeFactory.build("composite", center, r1)
        cm2 = ShapeFactory.build("composite", center, t1, c1)
        cm3 = ShapeFactory.build("composite", center, cm1, e1, cm2)
        expected = cm3.toString()
        testShapeIO = ShapeIO()
        actual = testShapeIO.saveShape(cm3)
        self.assertEqual(expected, actual)

    def testLoadComposite(self):
        center = Point(0, 0)
        r1 = ShapeFactory.build("rectangle", Point(1, 1), Point(4, 1), Point(4, 3), Point(1, 3))
        t1 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))
        c1 = ShapeFactory.build("circle", Point(0, 0), Point(2, 0), Point(0, 2))
        e1 = ShapeFactory.build("ellipse", Point(0, 0), Point(3, 0), Point(0, 2))
        cm1 = ShapeFactory.build("composite", center, r1)
        cm2 = ShapeFactory.build("composite", center, t1, c1)
        cm3 = ShapeFactory.build("composite", center, cm1, e1, cm2)
        expected = cm3
        testShapeIO = ShapeIO()
        composite_string = "composite,0,0,begin," \
                                "composite,0,0,begin," \
                                    "rectangle,2.5,2.0,1,1,4,1,4,3,1,3," \
                                "end," \
                                "ellipse,0,0,3,0,0,2," \
                                "composite,0,0,begin," \
                                    "triangle,3.0,2.25,1,2,5,1,3,3," \
                                    "circle,0,0,2,0,0,2," \
                                "end," \
                           "end"
        actual = testShapeIO.loadShape(composite_string)
        self.assertEqual(expected, actual)
