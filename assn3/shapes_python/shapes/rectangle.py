#!/usr/bin/env python3

"""
Rectangle

This class represents rectangle objects that can be moved.
Users of a rectangle can also compute its area, height, and width.
"""
from shapes.line import Line
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Rectangle:
    def __init__(self, *args, **kwargs):
        try: # Construct with x1, y1, x2, y2, x3, y3, x4, y4
            if not self.__constructWithPoints(args[0], args[1], args[2], args[3]):
                if not self.__constructWithLines(args[0], args[1], args[2], args[3]):
                    if not self.__constructWithCoords(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7]):
                        raise ShapeException("Rectangle construction failed")
        except IndexError:
            raise ShapeException("Invalid arguments for shape construction")

    def __constructWithCoords(self, x1, y1, x2, y2, x3, y3, x4, y4):
        try:
            self.__line1 = Line(x1, y1, x2, y2)
            self.__line2 = Line(x2, y2, x3, y3)
            self.__line3 = Line(x3, y3, x4, y4)
            self.__line4 = Line(x4, y4, x1, y1)
            Rectangle.validateRectangle(value=self, errorMessage="Invalid Rectangle")
            return True
        except ShapeException:
            return False

    def __constructWithPoints(self, point1, point2, point3, point4):
        try:
            self.__line1 = Line(point1, point2)
            self.__line2 = Line(point2, point3)
            self.__line3 = Line(point3, point4)
            self.__line4 = Line(point4, point1)
            Rectangle.validateRectangle(value=self, errorMessage="Invalid Rectangle")
            return True
        except ShapeException:
            return False

    def __constructWithLines(self, line1, line2, line3, line4):
        try:
            self.__line1 = line1
            self.__line2 = line2
            self.__line3 = line3
            self.__line4 = line4
            Rectangle.validateRectangle(value=self, errorMessage="Invalid Rectangle")
            return True
        except ShapeException:
            return False

    @staticmethod
    def validateRectangle(value, errorMessage):
        if not isinstance(value, Rectangle):
            raise ShapeException(errorMessage)

        Line.validateLine(value.line1, "Line 1 is not a valid line.")
        Line.validateLine(value.line2, "Line 2 is not a valid line.")
        Line.validateLine(value.line3, "Line 3 is not a valid line.")
        Line.validateLine(value.line4, "Line 4 is not a valid line.")

        Validator.validateLinesFormLoop([value.line1, value.line2, value.line3, value.line4], "Lines do not form an enclosed rectangle.")

        Validator.validateLinesFormRightAngles([value.line1, value.line2, value.line3, value.line4], "Lines do not form 90 degree angles.")

    
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
    def point4(self):
        return self.__line4.point1

    @property
    def line1(self):
        return self.__line1

    @property
    def line2(self):
        return self.__line2

    @property
    def line3(self):
        return self.__line3

    @property
    def line4(self):
        return self.__line4

    def move(self, deltaX, deltaY):
        self.__line1.move(deltaX, deltaY)
        self.__line2.move(deltaX, deltaY)
        self.__line3.move(deltaX, deltaY)
        self.__line4.move(deltaX, deltaY)

    def computeWidth(self):
        return self.__line1.computeLength()

    def computeHeight(self):
        return self.__line2.computeLength()

    def computeArea(self):
        return self.computeWidth() * self.computeHeight()

