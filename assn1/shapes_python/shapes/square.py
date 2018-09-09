#!/usr/bin/env python3

"""
Square

This class represents square objects that can be moved.
Users of a square can also compute its area, height, and width.
"""

import math

class Square(Rectangle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        Validator.validateSquare(self, "Square is invalid")

