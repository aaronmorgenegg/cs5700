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

