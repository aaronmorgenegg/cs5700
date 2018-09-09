#!/usr/bin/env python3

"""
Ellipse

This class represents ellipse objects that can be moved and scaled.
Users of an ellipse can also compute its area.
"""
from shapes.point import Point
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


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

    def __constructWithCoords(self, x1, y1, x2, y2, x3, y3):
        self.__center = Point(x1, y1)
        focus1 = Point(x2, y2)
        focus2 = Point(x3, y3)
        mirror1 = self.__getMirrorFocus(self.__center, focus1)
        mirror2 = self.__getMirrorFocus(self.__center, focus2)
        self.__foci1 = (focus1, mirror1)
        self.__foci2 = (focus2, mirror2)

    def __constructWithPoints(self, point1, point2, point3):
        self.__center = point1
        focus1 = point2
        focus2 = point3
        mirror1 = self.__getMirrorFocus(self.__center, focus1)
        mirror2 = self.__getMirrorFocus(self.__center, focus2)
        self.__foci1 = (focus1, mirror1)
        self.__foci2 = (focus2, mirror2)

    def __getMirrorFocus(self, center, focus):
        Validator.validatePoint(center, "Center point invalid")
        Validator.validatePoint(focus, "Focus point invalid")
        dx = focus.x - center.x
        dy = focus.y - center.y
        x = focus.x - dx*2
        y = focus.y - dy*2
        return Point(x, y)

    @property
    def center(self):
        return self.__center

    @property
    def foci1(self):
        return self.__foci1

    @property
    def foci2(self):
        return self.__foci2

    @property
    def focus1(self):
        return self.__foci1[0]

    @property
    def focus2(self):
        return self.__foci2[0]

    def move(self, deltaX, deltaY):
        self.__center.move(deltaX, deltaY)
        self.__focus1.move(deltaX, deltaY)
        self.__focus2.move(deltaX, deltaY)

    def computeArea(self):
        return 1 # TODO

    def scale(self, scaleFactor):
        Validator.validatePositiveDouble(scaleFactor())
        f1_dx = self.__focus1.x - self.__center.x
        f1_dy = self.__focus1.y - self.__center.y
        f2_dx = self.__focus2.x - self.__center.x
        f2_dy = self.__focus2.y - self.__center.y
        self.__focus1.x = f1_dx*scaleFactor + self.__center.x
        self.__focus1.y = f1_dy*scaleFactor + self.__center.y
        self.__focus2.x = f2_dx*scaleFactor + self.__center.x
        self.__focus2.y = f2_dy*scaleFactor + self.__center.y

