#!/usr/bin/env python3

"""
Rectangle

This class represents rectangle objects that can be moved.
Users of a rectangle can also compute its area, height, and width.
"""

import math

class Rectangle:
    def __init__(self, *args, **kwargs):
        try: # Construct with x1, y1, x2, y2, x3, y3, x4, y4
            self.__constructWithCoords(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])
        except ShapeException:
            pass
        try: # Construct with point1, point2, point3, point4
            self.__constructWithPoints(args[0], args[1], args[2], args[3])
        except ShapeException:
            pass
        # Construct with line1, line2, line3, line4
        self.__constructWithLines(args[0], args[1], args[2], args[3])

        Validator.validateRectangle(self, "Rectangle is invalid")

    def __constructWithCoords(x1, y1, x2, y2, x3, y3, x4, y4):
        self.__line1 = Line(x1, y1, x2, y2)
        self.__line2 = Line(x2, y2, x3, y3)
        self.__line3 = Line(x3, y3, x4, y4)
        self.__line4 = Line(x4, y4, x1, y1)

    def __constructWithPoints(point1, point2, point3, point4):
        self.__line1 = Line(point1, point2)
        self.__line2 = Line(point2, point3)
        self.__line3 = Line(point3, point4)
        self.__line4 = Line(point4, point1)

    def __constructWithLines(line1, line2, line3, line4):
        self.__line1 = line1
        self.__line2 = line2
        self.__line3 = line3
        self.__line4 = line4
    
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

    def move(deltaX, deltaY):
        self.__line1.move(deltaX, deltaY)
        self.__line2.move(deltaX, deltaY)
        self.__line3.move(deltaX, deltaY)
        self.__line4.move(deltaX, deltaY)

    def computeWidth():
        return self.__line1.computeLength()

    def computeHeight():
        return self.__line2.computeLength()

    def computeArea():
        return self.computeWidth() * self.computeHeight()

