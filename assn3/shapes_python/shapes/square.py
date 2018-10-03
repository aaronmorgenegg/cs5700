#!/usr/bin/env python3

"""
Square

This class represents square objects that can be moved.
Users of a square can also compute its area, height, and width.
"""
from shapes.rectangle import Rectangle
from shapes.validator import Validator


class Square(Rectangle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        Square.validateSquare(self, "Square is invalid")

    @staticmethod
    def validateSquare(value, errorMessage):
        Rectangle.validateRectangle(value, errorMessage)

        Validator.validateLinesAreSameLength([value.line1, value.line2, value.line3, value.line4], "Lines of square are not same length.")


