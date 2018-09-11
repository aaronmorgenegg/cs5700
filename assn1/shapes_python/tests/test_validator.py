#!/usr/bin/env python3

import unittest

from shapes.circle import Circle
from shapes.ellipse import Ellipse
from shapes.line import Line
from shapes.point import Point
from shapes.rectangle import Rectangle
from shapes.shape_exception import ShapeException
from shapes.square import Square
from shapes.triangle import Triangle
from shapes.validator import Validator, isInfinite


class TestValidator(unittest.TestCase):
    def testIsInfinite(self):
        self.assertTrue(isInfinite(float('inf')))
        self.assertTrue(isInfinite(float('-inf')))
        self.assertFalse(isInfinite(0))
        self.assertFalse(isInfinite(1231245513632623.2134))
        self.assertFalse(isInfinite(-1234125125124512.2345))

    def testValidateDouble(self):
        Validator.validateDouble(123.456, "Double unexpectedly invalid")
        Validator.validateDouble(0, "Double unexpectedly invalid")
        Validator.validateDouble(-123.456, "Double unexpectedly invalid")

        self.assertRaises(ShapeException, Validator.validateDouble, None, "None is not a valid double")
        self.assertRaises(ShapeException, Validator.validateDouble, float('inf'), "Inf is not a valid double")
        self.assertRaises(ShapeException, Validator.validateDouble, float('-inf'), "-Inf is not a valid double")
        self.assertRaises(ShapeException, Validator.validateDouble, "foo", "String \'foo\' is not a valid double")

    def testValidatePositiveDouble(self):
        Validator.validatePositiveDouble(123.456, "Double unexpectedly invalid")
        Validator.validatePositiveDouble(0, "Double unexpectedly invalid")

        self.assertRaises(ShapeException, Validator.validatePositiveDouble,
                          None, "None is not a valid positive double")
        self.assertRaises(ShapeException, Validator.validatePositiveDouble,
                          float('inf'), "Inf is not a valid positive double")
        self.assertRaises(ShapeException, Validator.validatePositiveDouble,
                          float('-inf'), "-Inf is not a valid positive double")
        self.assertRaises(ShapeException, Validator.validatePositiveDouble,
                          "foo", "String \'foo\' is not a valid positive double")
        self.assertRaises(ShapeException, Validator.validatePositiveDouble,
                          -123.456, "-123.456 is not a valid positive double")

    def testValidatePoint(self):
        p1 = Point(1, 1)
        Validator.validatePoint(p1, "Point unexpectedly invalid")

        self.assertRaises(ShapeException, Validator.validatePoint, "(1, 1)",
                          "String \'(1, 1)\' is not a valid point")

    def testValidateLine(self):
        l1 = Line(1, 1, -1, -5)
        Validator.validateLine(l1, "Line unexpectedly invalid")

        self.assertRaises(ShapeException, Validator.validateLine, "(1, 1, -1, -5)",
                          "String \'(1, 1, -1, -5)\' is not a valid line")
        self.assertRaises(ShapeException, Validator.validateLine, Point(1, 1), "Point is not a valid line")

    def testValidateTriangle(self):
        t1 = Triangle(1, 1, -1, -5, -3, -2)
        Validator.validateTriangle(t1, "Triangle unexpectedly invalid")

        self.assertRaises(ShapeException, Validator.validateLine, "(1, 1, -1, -5, -3, -2)",
                          "String \'(1, 1, -1, -5, -3, -2)\' is not a valid triangle")
        self.assertRaises(ShapeException, Validator.validateLine, Point(1, 1), "Point is not a valid triangle")

    def testValidateRectangle(self):
        r1 = Rectangle(1, 1, 4, 1, 4, 3, 1, 3)
        Validator.validateRectangle(r1, "Rectangle unexpectedly invalid")

        self.assertRaises(ShapeException, Validator.validateRectangle, "(1, 1, 4, 1, 4, 3, 1, 3)",
                          "String \'(1, 1, 4, 1, 4, 3, 4, 3)\' is not a valid rectangle")
        self.assertRaises(ShapeException, Validator.validateRectangle, Point(1, 1), "Point is not a valid rectangle")

    def testValidateRectangle(self):
        s1 = Square(1, 1, 3, 1, 3, 3, 1, 3)
        Validator.validateSquare(s1, "Square unexpectedly invalid")

        self.assertRaises(ShapeException, Validator.validateSquare, "(1, 1, 3, 1, 3, 3, 1, 3)",
                          "String \'(1, 1, 3, 1, 3, 3, 3, 3)\' is not a valid square")
        self.assertRaises(ShapeException, Validator.validateSquare, Point(1, 1), "Point is not a valid square")

    def testValidateEllipse(self):
        e1 = Ellipse(0, 0, 2, 0, 0, 1, 3, 0, 0, 2)
        Validator.validateEllipse(e1, "Ellipse unexpectedly invalid")

        self.assertRaises(ShapeException, Validator.validateEllipse, "(0, 0, 2, 0, 1, 0, 3, 0, 0, 2)",
                          "String \'(0, 0, 2, 0, 0, 1, 3, 0, 0, 2)\' is not a valid ellipse")
        self.assertRaises(ShapeException, Validator.validateEllipse, Point(1, 1), "Point is not a valid ellipse")

    def testValidateCircle(self):
        c1 = Circle(0, 0, 2, 0, 0, 2, 3, 0, 0, 3)
        Validator.validateCircle(c1, "Circle unexpectedly invalid")

        self.assertRaises(ShapeException, Validator.validateCircle, "(0, 0, 2, 0, 0, 2, 3, 0, 0, 3)",
                          "String \'(0, 0, 2, 0, 0, 2, 3, 0, 0, 3)\' is not a valid circle")
        self.assertRaises(ShapeException, Validator.validateCircle, Point(1, 1), "Point is not a valid circle")
