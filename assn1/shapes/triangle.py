#!/usr/bin/env python3

"""
Triangle

This class represents triangle objects that can be moved.
Users of a triangle can also compute its area.
"""

import math

class Triangle:
    def __init__(self, *args, **kwargs):
        try: # Construct with x1, y1, x2, y2, x3, y3
            self.__constructWithCoords(args[0], args[1], args[2], args[3], args[4], args[5])
        except ShapeException:
            pass
        try: # Construct with point1, point2, point3
            self.__constructWithPoints(args[0], args[1], args[2])
        except ShapeException:
            pass
        # Construct with line1, line2, line3
        self.__constructWithLines(args[0], args[1], args[2])

        Validator.validateTriangle(self, "Triangle is invalid")

    def __constructWithCoords(x1, y1, x2, y2, x3, y3):
        self.__line1 = Line(x1=x1, y1=y1, x2=x2, y2=y2)
        self.__line2 = Line(x1=x2, y1=y2, x2=x3, y2=y3)
        self.__line3 = Line(x1=x3, y1=y3, x2=x1, y2=y1)

    def __constructWithPoints(point1, point2, point3):
        self.__line1 = Line(point1=point1, point2=point2)
        self.__line2 = Line(point1=point2, point2=point3)
        self.__line3 = Line(point1=point3, point2=point1)

    def __constructWithLines(line1, line2, line3):
        self.__line1 = line1
        self.__line2 = line2
        self.__line3 = line3
    
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

    def move(deltaX, deltaY):
        self.__line1.move(deltaX, deltaY)
        self.__line2.move(deltaX, deltaY)
        self.__line3.move(deltaX, deltaY)

    def computeArea():
        """Compute area using Heron's formula"""
        a = self.__line1.computeLength()
        b = self.__line2.computeLength()
        c = self.__line3.computeLength()
        s = (a+b+c)/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))

