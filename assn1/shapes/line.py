#!/usr/bin/env python3

"""
Line

This class represents line objects that can be moved.
Users of a line can also get its length and slope.
"""

import math

class Line:
    def __init__(self, x1=None, y1=None, x2=None, y2=None, point1=None, point2=None):
        try: # Construct with x1, y1, x2, y2
            self.__point1 = Point(x1, y1)
            self.__point2 = Point(x2, y2)
        except ShapeException: # Construct with point1, point2
            Validator.validatePoint(point1, "Invalid point1")
            Validator.validatePoint(point2, "Invalid point2")
            self.__point1 = point1
            self.__point2 = point2

        if self.__point1 == self.__point2:
            raise ShapeException("Line must have non-zero length.")
    
    @property
    def point1(self):
        return self.__point1

    @point1.setter
    def point1(self, value):
        self.__point1 = value

    @property
    def point2(self):
        return self.__point2

    @point2.setter
    def point2(self, value):
        self.__point2 = value

    def move(deltaX, deltaY):
        self.point1.move(deltaX, deltaY)
        self.point2.move(deltaX, deltaY)

    def computeLength():
        return math.sqrt( ((self.point1.x - self.point2.x)**2) + ((self.point1.y - self.point2.y)**2) )

    def computeSlope():
        return ( (self.point2.y - self.point1.y)/(self.point2.x - self.point1.x) )

  

