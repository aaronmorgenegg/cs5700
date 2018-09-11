#!/usr/bin/env python3

"""
Ellipse

This class represents ellipse objects that can be moved and scaled.
Users of an ellipse can also compute its area.
"""
from shapes.constants import PI
from shapes.line import Line
from shapes.point import Point
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Ellipse:
    def __init__(self, *args, **kwargs):
        """Expects arguments as center, focus1, focus2, edge1, edge2"""
        try:
            if not self.__constructWithPoints(args[0], args[1], args[2], args[3], args[4]):
                if not self.__constructWithCoords(args[0], args[1], args[2], args[3], args[4],
                                                  args[5], args[6], args[7], args[8], args[9]):
                    raise ShapeException("Ellipse construction failed")
        except IndexError:
            raise ShapeException("Invalid arguments for ellipse construction")

    def __constructWithCoords(self, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
        try:
            self.__center = Point(x1, y1)
            focus1 = Point(x2, y2)
            focus2 = Point(x3, y3)
            mirror1 = self.__getMirrorFocus(self.__center, focus1)
            mirror2 = self.__getMirrorFocus(self.__center, focus2)
            self.__foci1 = [focus1, mirror1]
            self.__foci2 = [focus2, mirror2]
            self.__axis1 = Line(self.__center.copy(), Point(x4, y4))
            self.__axis2 = Line(self.__center.copy(), Point(x5, y5))
            Validator.validateEllipse(value=self, errorMessage="Ellipse is invalid")
            return True
        except ShapeException:
            return False

    def __constructWithPoints(self, point1, point2, point3, point4, point5):
        try:
            self.__center = point1
            focus1 = point2
            focus2 = point3
            mirror1 = self.__getMirrorFocus(self.__center, focus1)
            mirror2 = self.__getMirrorFocus(self.__center, focus2)
            self.__foci1 = [focus1, mirror1]
            self.__foci2 = [focus2, mirror2]
            self.__axis1 = Line(self.__center.copy(), point4)
            self.__axis2 = Line(self.__center.copy(), point5)
            Validator.validateEllipse(value=self, errorMessage="Ellipse is invalid")
            return True
        except ShapeException:
            return False

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

    @property
    def axis1(self):
        return self.__axis1

    @property
    def axis2(self):
        return self.__axis2

    @property
    def edge1(self):
        return self.__axis1.point2

    @property
    def edge2(self):
        return self.__axis2.point2

    def move(self, deltaX, deltaY):
        self.center.move(deltaX, deltaY)
        self.focus1.move(deltaX, deltaY)
        self.focus2.move(deltaX, deltaY)
        self.axis1.move(deltaX, deltaY)
        self.axis2.move(deltaX, deltaY)

    def computeArea(self):
        return PI * self.axis1.computeLength() * self.axis2.computeLength()

    def scale(self, scaleFactor):
        Validator.validatePositiveDouble(scaleFactor, "Scale Factor not a valid double")
        f1_dx = self.foci1[0].x - self.__center.x
        f1_dy = self.foci1[0].y - self.__center.y
        f2_dx = self.foci2[0].x - self.__center.x
        f2_dy = self.foci2[0].y - self.__center.y
        a1_dx = self.axis1.point2.x - self.__center.x
        a1_dy = self.axis1.point2.y - self.__center.y
        a2_dx = self.axis2.point2.x - self.__center.x
        a2_dy = self.axis2.point2.y - self.__center.y
        self.foci1[0].x = f1_dx*scaleFactor + self.__center.x
        self.foci1[0].y = f1_dy*scaleFactor + self.__center.y
        self.foci1[1].x = f1_dx*scaleFactor + self.__center.x
        self.foci1[1].y = f1_dy*scaleFactor + self.__center.y
        self.foci2[0].x = f2_dx*scaleFactor + self.__center.x
        self.foci2[0].y = f2_dy*scaleFactor + self.__center.y
        self.foci2[1].x = f2_dx*scaleFactor + self.__center.x
        self.foci2[1].y = f2_dy*scaleFactor + self.__center.y
        self.axis1.point2.x = a1_dx*scaleFactor + self.__center.x
        self.axis1.point2.y = a1_dy*scaleFactor + self.__center.y
        self.axis2.point2.x = a2_dx*scaleFactor + self.__center.x
        self.axis2.point2.y = a2_dy*scaleFactor + self.__center.y
