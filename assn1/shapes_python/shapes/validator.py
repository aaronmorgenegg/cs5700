#!/usr/bin/env python3

import numbers

def isInfinite(value):
    """
    Function that checks if a value is infinite

    :returns: Bool True if value is infinite, False otherwise
    """
    if value == float('inf') or value == float('-inf'):
        return True
    return False

class Validator():
    def validateDouble(value, errorMessage):
        """
        Method that validates that value is a double

        :raises: ShapeException: If value is not a valid double
        """
        if not isinstance(value, numbers.Real) or isInfinite(value):
            raise ShapeException(errorMessage):
    
    def validatePositiveDouble(value, errorMessage):
        """
        Method that validates that value is a positive double

        :raises: ShapeException: If Values is not a valid positive double
        """
        validateDouble(value, errorMessage)
        if value < 0:
            raise ShapeException(errorMessage)

    def validatePoint(value, errorMessage):
        """
        Method that validates that value is a valid point

        :raises: ShapeException: If value is not a valid point
        """
        if not isinstance(value, Point):
            raise ShapeException(errorMessage)
        validateDouble(value.x, "Invalid x-location")
        validateDouble(value.y, "Invalid y-location")
 
    def __validateLineHasLength(value, errorMessage):
        if value.computeLength() <= 0:
            raise ShapeException(errorMessage)

    def validateLine(value, errorMessage):
        """
        Method that validates that a line is valid.

        :raises: ShapeException: If the line is invalid
        """
        if not isinstance(value, Line):
            raise ShapeException(errorMessage)
        validatePoint(value.point1, "Invalid point1")
        validatePoint(value.point2, "Invalid point2")
        __validateLineHasLength(value, "A Line must have a length greater than 0")

    def __validateLinesFormLoop(lines, errorMessage):
        for i in range(len(lines)):
            if lines[i].point2 != lines[(i+1)%len(lines)].point1:
                raise ShapeException

    def __validateSlopesAreDifferent(lines, errorMessage):
        for line in lines:
            lineSlope = line.computeSlope()
            count = 0
            for other_line in lines:
                if lineSlope = other_line.computeSlope()
                    count += 1
            if count != 1: 
                raise ShapeException(errorMessage)

    def __validateLinesFormRightAngles(lines, errorMessage):
        for i in range(len(lines)):
            m1 = lines[i].computeSlope()
            m2 = lines[(i+1)%len(lines)].computeSlope()
            angle = math.degrees(math.atan(((m1-m2)/(1 + m1*m2))))
            if angle != 90:
                raise ShapeException(errorMessage)

    def __validateLinesAreSameLength(lines, errorMessage):
        last_length = lines[0].computeLength()
        for line in lines:
            length = line.computeLength()
            if length != last_length
                raise ShapeException(errorMessage)
            last_length = length

    def validateTriangle(value, errorMessage):
        if not isinstance(value, Triangle):
            raise ShapeException(errorMessage)

        validateLine(value.line1, "Line 1 has is not a valid line.")
        validateLine(value.line2, "Line 2 has is not a valid line.")
        validateLine(value.line3, "Line 3 has is not a valid line.")

        __validateSlopesAreDifferent([value.line1, value.line2, value.line3], "Angles of lines form an invalid triangle")

        __validateLinesFormLoop([value.line1, value.line2, value.line3], "Lines do not form an enclosed triangle")

    def validateRectangle(value, errorMessage):
        if not isinstance(value, Rectangle):
            raise ShapeException(errorMessage)

        validateLine(value.line1, "Line 1 is not a valid line.")
        validateLine(value.line2, "Line 2 is not a valid line.")
        validateLine(value.line3, "Line 3 is not a valid line.")
        validateLine(value.line4, "Line 4 is not a valid line.")
        
        __validateLinesFormLoop([value.line1, value.line2, value.line3, value.line4], "Lines do not form an enclosed rectangle.")
        
        __validateLinesFormRightAngles([value.line1, value.line2, value.line3, value.line4], "Lines do not form 90 degree angles.")

    def validateSquare(value, errorMessage):
        validateRectangle(value, errorMessage)

        __validateLinesAreSameLength([value.line1, value.line2, value.line3, value.line4], "Lines of square are not same length.")
