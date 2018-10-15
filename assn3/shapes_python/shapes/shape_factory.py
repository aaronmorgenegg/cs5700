#!/usr/bin/env python3

"""
Shape Factory

Class the constructs shape objects.
"""
from shapes.circle import Circle
from shapes.composite import Composite
from shapes.ellipse import Ellipse
from shapes.image import Image
from shapes.line import Line
from shapes.rectangle import Rectangle
from shapes.shape_exception import ShapeException
from shapes.square import Square
from shapes.triangle import Triangle

SHAPE_FACTORY_MAP = {
            'line': Line,
            'triangle': Triangle,
            'rectangle': Rectangle,
            'square': Square,
            'ellipse': Ellipse,
            'circle': Circle,
            'composite': Composite,
            'image': Image
                     }


class ShapeFactory:
    @staticmethod
    def build(type, *args, **kwargs):
        try:
            shape_class = SHAPE_FACTORY_MAP[type]
        except KeyError:
            raise ShapeException('Error: Invalid type for shape factory construction')

        return shape_class(*args, **kwargs)
