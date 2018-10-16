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
        center = Point(0, 0)
        r1 = ShapeFactory.build("rectangle", Point(1, 1), Point(4, 1), Point(4, 3), Point(1, 3))
        t1 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))
        c1 = ShapeFactory.build("circle", Point(0, 0), Point(2, 0), Point(0, 2))
        e1 = ShapeFactory.build("ellipse", Point(0, 0), Point(3, 0), Point(0, 2))
        l1 = ShapeFactory.build("line", Point(4, 2), Point(6, 1))
        cm1 = ShapeFactory.build("composite", center, r1)
        expected = r1.computeArea()
        actual = cm1.computeArea()
        self.assertEqual(expected, actual)

        cm2 = ShapeFactory.build("composite", center, t1, c1)
        expected = t1.computeArea() + c1.computeArea()
        actual = cm2.computeArea()
        self.assertEqual(expected, actual)

        cm3 = ShapeFactory.build("composite", center, cm1, e1, cm2)
        expected = cm1.computeArea() + e1.computeArea() + cm2.computeArea()
        actual = cm3.computeArea()
        self.assertEqual(expected, actual)

        cm4 = ShapeFactory.build("composite", center)
        expected = 0
        actual = cm4.computeArea()
        self.assertEqual(expected, actual)

        cm5 = ShapeFactory.build("composite", center, l1, r1)
        expected = r1.computeArea()
        actual = cm5.computeArea()
        self.assertEqual(expected, actual)

    def testAddShape(self):
        center = Point(0, 0)
        cm1 = ShapeFactory.build("composite", center)
        self.assertEqual(0, len(cm1.shapes))
        r1 = ShapeFactory.build("rectangle", Point(1, 1), Point(4, 1), Point(4, 3), Point(1, 3))
        t1 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))
        cm1.addShape(r1)
        self.assertEqual(cm1.getShape(0), r1)
        cm1.addShape(t1)
        self.assertEqual(cm1.getShape(1), t1)

    def testRemoveshape(self):
        center = Point(0, 0)
        t1 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))
        c1 = ShapeFactory.build("circle", Point(0, 0), Point(2, 0), Point(0, 2))
        cm1 = ShapeFactory.build("composite", center, t1, c1)
        self.assertEqual(cm1.getShape(0), t1)
        self.assertEqual(cm1.getShape(1), c1)

        cm1.removeShape(1)
        self.assertEqual(cm1.getShape(0), t1)
        self.assertEqual(len(cm1.shapes), 1)

        cm1.removeShape(0)
        self.assertEqual(len(cm1.shapes), 0)

        self.assertRaises(ShapeException, cm1.removeShape, 3)

    def testClearShapes(self):
        center = Point(0, 0)
        t1 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))
        c1 = ShapeFactory.build("circle", Point(0, 0), Point(2, 0), Point(0, 2))
        cm1 = ShapeFactory.build("composite", center, t1, c1)
        self.assertEqual(cm1.getShape(0), t1)
        self.assertEqual(cm1.getShape(1), c1)
        self.assertEqual(len(cm1.shapes), 2)

        cm1.clearShapes()
        self.assertEqual(len(cm1.shapes), 0)

    def testGetShape(self):
        center = Point(0, 0)
        t1 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))
        c1 = ShapeFactory.build("circle", Point(0, 0), Point(2, 0), Point(0, 2))
        cm1 = ShapeFactory.build("composite", center, t1, c1)
        self.assertEqual(cm1.getShape(0), t1)
        self.assertEqual(cm1.getShape(1), c1)
        self.assertRaises(ShapeException, cm1.getShape, 2)

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
