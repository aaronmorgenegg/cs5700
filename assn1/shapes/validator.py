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
        Validator.validateDouble(value.x, "Invalid x-location")
        Validator.validateDouble(value.y, "Invalid y-location")
 

    def validatePointsAreUnique(points, errorMessage):
        """
        Method that validates that each given point has a unique position

        :raises: ShapeException: If any of the points are invalid or share positions
        """
        try:
            for point in points:
                validatePoint(point, "Invalid point")
                unique_count = 0
                for other_point in points:
                    if point == other_point:
                        unique_count += 1
                if unique_count > 1: # More than 1 point in a unique location
                    raise ShapeException(errorMessage)
        except TypeError: # Not given a list of points
            raise ShapeException(errorMessage)
       
    def validateLine(value, errorMessage):
        """
        Method that validates that a line is valid.

        :raises: ShapeException: If the line is invalid
        """
        if not isinstance(value, Line):
            raise ShapeException(errorMessage)
        Validator.validatePoint(value.point1, "Invalid point1")
        Validator.validatePoint(value.point2, "Invalid point2")
        Validator.validatePointsAreUnique([value.point1, value.point2], "A Line must have a length greater than 0")

    def validateLinesFormLoop(lines, errorMessage):
        for i in range(len(lines)):
            if lines[i].point2 != lines[(i+1)%len(lines)].point1:
                raise ShapeException

    def validateSlopesAreDifferent(lines, errorMessage):
        for line in lines:
            lineSlope = line.computeSlope()
            count = 0
            for other_line in lines:
                if lineSlope = other_line.computeSlope()
                    count += 1
            if count != 1: 
                raise ShapeException(errorMessage)

    def validateTriangle(value, errorMessage):
        if not isinstance(value, Triangle):
            raise ShapeException(errorMessage)

        Validator.validateLine(value.line1, "Line 1 has is not a valid line.")
        Validator.validateLine(value.line2, "Line 2 has is not a valid line.")
        Validator.validateLine(value.line3, "Line 3 has is not a valid line.")

        Validator.validateSlopesAreDifferent([value.line1, value.line2, value.line3], "Angles of lines form an invalid triangle")

        Validator.validateLinesFormLoop([value.line1, value.line2, value.line3], "Lines do not form an enclosed triangle")

