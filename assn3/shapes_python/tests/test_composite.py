#!/usr/bin/env python3

import unittest

from shapes.composite import Composite
from shapes.point import Point
from shapes.shape_exception import ShapeException
from shapes.shape_factory import ShapeFactory


class TestRectangle(unittest.TestCase):
    def testValidateComposite(self):
        center = Point(0,0)
        r1 = ShapeFactory.build("rectangle", Point(1, 1), Point(4, 1), Point(4, 3), Point(1, 3))
        t1 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))
        c1 = ShapeFactory.build("circle", Point(0, 0), Point(2, 0), Point(0, 2))
        e1 = ShapeFactory.build("ellipse", Point(0, 0), Point(3, 0), Point(0, 2))
        cm1 = ShapeFactory.build("composite", center, r1, t1, c1, e1)
        Composite.validateComposite(cm1, "Composite unexpectedly invalid")

        self.assertRaises(ShapeException, Composite.validateComposite, "(dummy composite)",
                          "String \'(dummy composite)\' is not a valid composite")
        self.assertRaises(ShapeException, Composite.validateComposite, Point(1, 1), "Point is not a valid composite")

    def testValidConstruction(self):
        center = Point(0,0)
        r1 = ShapeFactory.build("rectangle", Point(1, 1), Point(4, 1), Point(4, 3), Point(1, 3))
        t1 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))
        c1 = ShapeFactory.build("circle", Point(0, 0), Point(2, 0), Point(0, 2))
        e1 = ShapeFactory.build("ellipse", Point(0, 0), Point(3, 0), Point(0, 2))
        cm1 = ShapeFactory.build("composite", center, r1)
        self.assertEqual(center, cm1.center)
        self.assertEqual(cm1.getShape(0), r1)

        cm2 = ShapeFactory.build("composite", center, t1, c1)
        self.assertEqual(center, cm2.center)
        self.assertEqual(cm2.getShape(0), t1)
        self.assertEqual(cm2.getShape(1), c1)

        cm3 = ShapeFactory.build("composite", center, cm1, e1, cm2)
        self.assertEqual(center, cm3.center)
        self.assertEqual(cm3.getShape(0), cm1)
        self.assertEqual(cm3.getShape(1), e1)
        self.assertEqual(cm3.getShape(2), cm2)

        cm4 = ShapeFactory.build("composite", center)
        self.assertEqual(center, cm4.center)

    def testInvalidConstruction(self):
        pass # TODO

    def testMove(self):
        pass # TODO

    def testComputeArea(self):
        pass # TODO

    def testAddShape(self):
        pass # TODO

    def testRemoveshape(self):
        pass # TODO

    def testClearShapes(self):
        pass # TODO

    def testGetShape(self):
        pass # TODO

    def testToString(self):
        center = Point(0,0)
        r1 = ShapeFactory.build("rectangle", Point(1, 1), Point(4, 1), Point(4, 3), Point(1, 3))
        t1 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))
        c1 = ShapeFactory.build("circle", Point(0, 0), Point(2, 0), Point(0, 2))
        e1 = ShapeFactory.build("ellipse", Point(0, 0), Point(3, 0), Point(0, 2))
        cm1 = ShapeFactory.build("composite", center, r1)
        cm2 = ShapeFactory.build("composite", center, t1, c1)
        cm3 = ShapeFactory.build("composite", center, cm1, e1, cm2)
        expected = "composite,0,0,begin," \
                        "composite,0,0,begin," \
                            "rectangle,2.5,2.0,1,1,4,1,4,3,1,3," \
                        "end," \
                        "ellipse,0,0,3,0,0,2," \
                        "composite,0,0,begin," \
                            "triangle,3.0,2.25,1,2,5,1,3,3," \
                            "circle,0,0,2,0,0,2," \
                        "end," \
                   "end"
        actual = cm3.toString()
        self.assertEqual(expected, actual)
