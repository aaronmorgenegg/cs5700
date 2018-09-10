#!/usr/bin/env python3

"""
Triangle

This class represents triangle objects that can be moved.
Users of a triangle can also compute its area.
"""

import math

from shapes.line import Line
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Triangle:
    def __init__(self, *args, **kwargs):
        try:
            if not self.__constructWithPoints(args[0], args[1], args[2]):
                if not self.__constructWithLines(args[0], args[1], args[2]):
                    if not self.__constructWithCoords(args[0], args[1], args[2], args[3], args[4], args[5]):
                        raise ShapeException("Triangle construction failed")
        except IndexError:
            raise ShapeException("Invalid arguments for triangle construction")

    def __constructWithCoords(self, x1, y1, x2, y2, x3, y3):
        try:
            self.__line1 = Line(x1, y1, x2, y2)
            self.__line2 = Line(x2, y2, x3, y3)
            self.__line3 = Line(x3, y3, x1, y1)
            Validator.validateTriangle(value=self, errorMessage="Triangle invalid")
            return True
        except ShapeException:
            return False

    def __constructWithPoints(self, point1, point2, point3):
        try:
            self.__line1 = Line(point1, point2)
            self.__line2 = Line(point2, point3)
            self.__line3 = Line(point3, point1)
            Validator.validateTriangle(value=self, errorMessage="Triangle invalid")
            return True
        except ShapeException:
            return False

    def __constructWithLines(self, line1, line2, line3):
        try:
            self.__line1 = line1
            self.__line2 = line2
            self.__line3 = line3
            Validator.validateTriangle(value=self, errorMessage="Triangle invalid")
            return True
        except ShapeException:
            return False
    
    @property
    def point1(self):
        return self.__line1.point1

    @property
    def point2(self):
        return self.__line2.point1

    @property
    def point3(self):
        return self.__line3.point1

    @property
    def line1(self):
        return self.__line1

    @property
    def line2(self):
        return self.__line2

    @property
    def line3(self):
        return self.__line3

    def move(self, deltaX, deltaY):
        self.__line1.move(deltaX, deltaY)
        self.__line2.move(deltaX, deltaY)
        self.__line3.move(deltaX, deltaY)

    def computeArea(self):
        """Compute area using Heron's formula"""
        a = self.__line1.computeLength()
        b = self.__line2.computeLength()
        c = self.__line3.computeLength()
        s = (a+b+c)/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))

