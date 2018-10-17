#!/usr/bin/env python3

"""
Image Shape

This class represents embedded image shapes that contain an image.
Users of an image shape can also compute its area
"""
from shapes.image_cache import ImageCache
from shapes.rectangle import Rectangle
from shapes.shape_exception import ShapeException
from shapes.validator import Validator


class Image(Rectangle):
    image_cache = ImageCache()

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
        return Image.image_cache.loadSource(self.source)

    def draw(self, graphics):
        image = self.loadSource()
        graphics.imshow(image, extent=[self.point1.x, self.point1.y, self.point3.y, self.point3.x], aspect='auto')
