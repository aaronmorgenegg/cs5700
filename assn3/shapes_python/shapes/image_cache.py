#!/usr/bin/env python3

"""
Image Shape

This class represents embedded image shapes that contain an image.
Users of an image shape can also compute its area
"""
import os.path
import matplotlib.image as mpimg
from shapes.shape_exception import ShapeException


class ImageCache:
    def __init__(self):
        self.images = {}

    def loadSource(self, source):
        try:
            return self.images[source]
        except KeyError:
            image = self._loadFile(source)
            self.images[source] = image
            return image

    def _loadFile(self, source):
        if not os.path.isfile(source):
            raise ShapeException('Source image not found')
        try:
            return mpimg.imread(source)
        except Exception as e:
            raise ShapeException(e)
