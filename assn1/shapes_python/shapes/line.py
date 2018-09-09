#!/usr/bin/env python3

"""
Line

This class represents line objects that can be moved.
Users of a line can also get its length and slope.
"""

import math

class Line:
    def __init__(self, *args, **kwargs):
        try: # Construct with x1, y1, x2, y2
            self.__constructWithCoords(args[0], args[1], args[2], args[3])
        except ShapeException:
            pass
        
        # Construct with point1, point2
        self.__constructWithPoints(args[0], args[1])

        Validator.validateLine(self, "Line is invalid")

    def __constructWithCoords(x1, y1, x2, y2):
        self.__point1 = Point(x1, y1)
        self.__point2 = Point(x2, y2)

    def __constructWithPoints(point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    @property
    def point1(self):
        return self.__point1

    @property
    def point2(self):
        return self.__point2

    def move(deltaX, deltaY):
        self.point1.move(deltaX, deltaY)
        self.point2.move(deltaX, deltaY)

    def computeLength():
        return math.sqrt( ((self.point1.x - self.point2.x)**2) + ((self.point1.y - self.point2.y)**2) )

    def computeSlope():
        return ( (self.point2.y - self.point1.y)/(self.point2.x - self.point1.x) )

  
