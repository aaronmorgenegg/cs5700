#!/usr/bin/env python3

"""
Ellipse

This class represents ellipse objects that can be moved and scaled.
Users of an ellipse can also compute its area.
"""

import math

class Ellipse:
    def __init__(self, *args, **kwargs):
        """Expects arguments as center, focus1, focus2"""
        try: # Construct with x1, y1, x2, y2, x3, y3
            self.__constructWithCoords(args[0], args[1], args[2], args[3], args[4], args[5])
        except ShapeException:
            pass
        try: # Construct with point1, point2, point3
            self.__constructWithPoints(args[0], args[1], args[2])
        except ShapeException:
            pass

        Validator.validateEllipse(self, "Ellipse is invalid")

    def __constructWithCoords(x1, y1, x2, y2, x3, y3):
        self.__center = Point(x1, y1)
        self.__focus1 = Point(x2, y2)
        self.__focus2 = Point(x3, y3)

    def __constructWithPoints(point1, point2, point3):
        self.__center = point1
        self.__focus1 = point2
        self.__focus2 = point3

    @property
    def center(self):
        return self.__center

    @property
    def focus1(self):
        return self.__focus1

    @property
    def focus2(self):
        return self.__focus2

    def move(deltaX, deltaY):
        self.__center.move(deltaX, deltaY)
        self.__focus1.move(deltaX, deltaY)
        self.__focus2.move(deltaX, deltaY)

    def computeArea():
        pass # TODO

