#!/usr/bin/env python3

"""
Line

This class represents line objects that can be moved.
Users of a line can also get its length and slope.
"""
import math

from shapes.point import Point
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Line:
    def __init__(self, *args, **kwargs):
        try:
            if not self.__constructWithPoints(args[0], args[1]):
                if not self.__constructWithCoords(args[0], args[1], args[2], args[3]):
                    raise ShapeException("Line Construction Failed")
        except IndexError: # If no construction method works, raise an exception
            raise ShapeException("Invalid number of arguments for line construction")

    def __constructWithCoords(self, x1, y1, x2, y2):
        try:
            self.__point1 = Point(x1, y1)
            self.__point2 = Point(x2, y2)
            Validator.validateLine(value=self, errorMessage="Line invalid")
            return True
        except ShapeException:
            return False

    def __constructWithPoints(self, point1, point2):
        try:
            Validator.validatePoint(point1, "Invalid point1")
            Validator.validatePoint(point2, "Invalid point2")
            self.__point1 = point1
            self.__point2 = point2
            Validator.validateLine(value=self, errorMessage="Line invalid")
            return True
        except ShapeException:
            return False

    @property
    def point1(self):
        return self.__point1

    @property
    def point2(self):
        return self.__point2

    def move(self, deltaX, deltaY):
        self.point1.move(deltaX, deltaY)
        self.point2.move(deltaX, deltaY)

    def computeLength(self):
        return math.sqrt( ((self.point1.x - self.point2.x)**2) + ((self.point1.y - self.point2.y)**2) )

    def computeSlope(self):
        numerator = self.point2.y - self.point1.y
        denominator = self.point2.x - self.point1.x
        try:
            return numerator/denominator
        except ZeroDivisionError:
            if numerator > 0:
                return float('inf')
            else:
                return float('-inf')

  

