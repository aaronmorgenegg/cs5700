#!/usr/bin/env python3
import numbers
import imghdr

from shapes.constants import VALID_IMAGES
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
    def validateLineHasLength(value, errorMessage):
        if value.computeLength() <= 0:
            raise ShapeException(errorMessage)

    @staticmethod
    def validateLinesFormLoop(lines, errorMessage):
        for i in range(len(lines)):
            if lines[i].point2 != lines[(i + 1) % len(lines)].point1:
                raise ShapeException(errorMessage)

    @staticmethod
    def validateSlopesAreDifferent(lines, errorMessage):
        for line in lines:
            lineSlope = line.computeSlope()
            count = 0
            for other_line in lines:
                if lineSlope == other_line.computeSlope():
                    count += 1
            if count != 1:
                raise ShapeException(errorMessage)

    @staticmethod
    def validateLinesFormRightAngles(lines, errorMessage):
        for i in range(len(lines)):
            m1 = lines[i].computeSlope()
            m2 = lines[(i+1)%len(lines)].computeSlope()
            if isInfinite(m1) or m1 == 0 or \
               isInfinite(m2) or m2 == 0:
                if isInfinite(m1) and m2 == 0 or \
                   isInfinite(m2) and m1 == 0:
                    pass
                else:
                    raise ShapeException(errorMessage)
            else:
                if round(m1, 2) != round(-1/m2, 2):
                    raise ShapeException(errorMessage)

    @staticmethod
    def validateLinesAreSameLength(lines, errorMessage):
        last_length = lines[0].computeLength()
        for line in lines:
            length = line.computeLength()
            if length != last_length:
                raise ShapeException(errorMessage)
            last_length = length

    @staticmethod
    def validateSource(source):
        """Validate a source for an image"""
        try:
            if imghdr.what(source) not in VALID_IMAGES:
                raise ShapeException('Source is not a valid image.')
        except TypeError:
            raise ShapeException('Source is not a valid image.')

