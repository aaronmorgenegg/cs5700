#!/usr/bin/env python3

"""
Image Shape

This class represents embedded image shapes that contain an image.
Users of an image shape can also compute its area
"""
from shapes.rectangle import Rectangle
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Image(Rectangle):
    def __init__(self, *args, **kwargs):
        self.source = args[-1]
        del args[-1]
        super().__init__(args, kwargs)
        Image.validateImage(self, "Image is invalid")

    @staticmethod
    def validateImage(value, errorMessage):
        if not isinstance(value, Image):
            raise ShapeException(errorMessage)\

        Validator.validateSource(value.source)

    def validate(self):
        return Image.validateImage(self, "Image is invalid")

    def toString(self, name="image"):
        return super().toString(name) + ", {}".format(self.source)
