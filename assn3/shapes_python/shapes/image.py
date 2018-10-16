#!/usr/bin/env python3

"""
Image Shape

This class represents embedded image shapes that contain an image.
Users of an image shape can also compute its area
"""
import matplotlib.image as mpimg
from shapes.rectangle import Rectangle
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Image(Rectangle):
    def __init__(self, *args, **kwargs):
        args_list = list(args)
        self.source = args_list.pop()
        super().__init__(*args_list, **kwargs)
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

    def loadSource(self):
        try:
            return mpimg.imread(self.source)
        except Exception as e:
            raise ShapeException(e)


    def draw(self, graphics):
        image = self.loadSource()
        graphics.imshow(image, extent=[self.point1.x, self.point1.y, self.point3.y, self.point3.x], aspect='auto')
