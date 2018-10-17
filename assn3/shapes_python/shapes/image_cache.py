#!/usr/bin/env python3

"""
Image Cache

This class represents image objects that are loaded from
an image. Each image is loaded once and shared between
many image shapes.
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
