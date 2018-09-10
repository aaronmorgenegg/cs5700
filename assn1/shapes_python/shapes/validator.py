#!/usr/bin/env python3
import math
import numbers

from shapes.shape_exception import ShapeException


def isInfinite(value):
    """
    Function that checks if a value is infinite

    :returns: Bool True if value is infinite, False otherwise
    """
    if value == float('inf') or value == float('-inf'):
        return True
    return False


class Validator:
    @staticmethod
    def validateDouble(value, errorMessage):
        """
        Method that validates that value is a double

        :raises: ShapeException: If value is not a valid double
        """
        if not isinstance(value, numbers.Real) or isInfinite(value):
            raise ShapeException(errorMessage)

    @staticmethod
    def validatePositiveDouble(value, errorMessage):
        """
        Method that validates that value is a positive double

        :raises: ShapeException: If Values is not a valid positive double
        """
        Validator.validateDouble(value, errorMessage)
        if value < 0:
            raise ShapeException(errorMessage)

    @staticmethod
    def validatePoint(value, errorMessage):
        """
        Method that validates that value is a valid point

        :raises: ShapeException: If value is not a valid point
        """
        from shapes.point import Point
        if not isinstance(value, Point):
            raise ShapeException(errorMessage)
        Validator.validateDouble(value.x, "Invalid x-location")
        Validator.validateDouble(value.y, "Invalid y-location")

    @staticmethod
    def validateLine(value, errorMessage):
        """
        Method that validates that a line is valid.

        :raises: ShapeException: If the line is invalid
        """
        from shapes.line import Line
        if not isinstance(value, Line):
            raise ShapeException(errorMessage)
        Validator.validatePoint(value.point1, "Invalid point1")
        Validator.validatePoint(value.point2, "Invalid point2")
        Validator.__validateLineHasLength(value, "A Line must have a length greater than 0")

    @staticmethod
    def validateTriangle(value, errorMessage):
        from shapes.triangle import Triangle
        if not isinstance(value, Triangle):
            raise ShapeException(errorMessage)

        Validator.validateLine(value.line1, "Line 1 has is not a valid line.")
        Validator.validateLine(value.line2, "Line 2 has is not a valid line.")
        Validator.validateLine(value.line3, "Line 3 has is not a valid line.")

        Validator.__validateSlopesAreDifferent([value.line1, value.line2, value.line3], "Angles of lines form an invalid triangle")

        Validator.__validateLinesFormLoop([value.line1, value.line2, value.line3], "Lines do not form an enclosed triangle")

    @staticmethod
    def validateRectangle(value, errorMessage):
        from shapes.rectangle import Rectangle
        if not isinstance(value, Rectangle):
            raise ShapeException(errorMessage)

        Validator.validateLine(value.line1, "Line 1 is not a valid line.")
        Validator.validateLine(value.line2, "Line 2 is not a valid line.")
        Validator.validateLine(value.line3, "Line 3 is not a valid line.")
        Validator.validateLine(value.line4, "Line 4 is not a valid line.")

        Validator.__validateLinesFormLoop([value.line1, value.line2, value.line3, value.line4], "Lines do not form an enclosed rectangle.")

        Validator.__validateLinesFormRightAngles([value.line1, value.line2, value.line3, value.line4], "Lines do not form 90 degree angles.")

    @staticmethod
    def validateSquare(value, errorMessage):
        Validator.validateRectangle(value, errorMessage)

        Validator.__validateLinesAreSameLength([value.line1, value.line2, value.line3, value.line4], "Lines of square are not same length.")

    @staticmethod
    def __validateLineHasLength(value, errorMessage):
        if value.computeLength() <= 0:
            raise ShapeException(errorMessage)

    @staticmethod
    def __validateLinesFormLoop(lines, errorMessage):
        for i in range(len(lines)):
            if lines[i].point2 != lines[(i + 1) % len(lines)].point1:
                raise ShapeException(errorMessage)

    @staticmethod
    def __validateSlopesAreDifferent(lines, errorMessage):
        for line in lines:
            lineSlope = line.computeSlope()
            count = 0
            for other_line in lines:
                if lineSlope == other_line.computeSlope():
                    count += 1
            if count != 1:
                raise ShapeException(errorMessage)

    @staticmethod
    def __validateLinesFormRightAngles(lines, errorMessage):
        for i in range(len(lines)):
            m1 = lines[i].computeSlope()
            m2 = lines[(i+1)%len(lines)].computeSlope()
            angle = math.degrees(math.atan(((m1-m2)/(1 + m1*m2))))
            if angle != 90:
                raise ShapeException(errorMessage)

    @staticmethod
    def __validateLinesAreSameLength(lines, errorMessage):
        last_length = lines[0].computeLength()
        for line in lines:
            length = line.computeLength()
            if length != last_length:
                raise ShapeException(errorMessage)
            last_length = length
