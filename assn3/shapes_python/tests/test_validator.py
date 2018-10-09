#!/usr/bin/env python3

import unittest

from shapes.shape_exception import ShapeException
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
