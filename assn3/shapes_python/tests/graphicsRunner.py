#!/usr/bin/env python3

"""
A manual testing script to draw shapes.

Run the script and verify that the shapes
look as they should.

python graphicsRunner.py
"""
import matplotlib.pyplot as graphics
from shapes.point import Point
from shapes.shape_factory import ShapeFactory


def setupGraphics():
    graphics.axis()


def drawLine(graphics):
    p1 = Point(-5, 3)
    p2 = Point(2, 4)
    l1 = ShapeFactory.build("line", p1, p2)
    l1.draw(graphics)
    graphics.show()


def drawTriangle(graphics):
    p1 = Point(1, -2)
    p2 = Point(2, -1)
    p3 = Point(0, 0)
    t1 = ShapeFactory.build("triangle", p1, p2, p3)
    t1.draw(graphics)
    graphics.show()


def drawRectangle(graphics):
    p1 = Point(1, 3)
    p2 = Point(5, 3)
    p3 = Point(5, 1)
    p4 = Point(1, 1)
    r1 = ShapeFactory.build("rectangle", p1, p2, p3, p4)
    r1.draw(graphics)
    graphics.show()

def drawSquare(graphics):
    p1 = Point(1, 3)
    p2 = Point(5, 3)
    p3 = Point(5, -1)
    p4 = Point(1, -1)
    s1 = ShapeFactory.build("square", p1, p2, p3, p4)
    s1.draw(graphics)
    graphics.show()

def drawEllipse(graphics):
    p1 = Point(0, 0)
    p2 = Point(3, 0)
    p3 = Point(0, 2)
    e1 = ShapeFactory.build("ellipse", p1, p2, p3)
    e1.draw(graphics)
    graphics.show()

def drawCircle(graphics):
    p1 = Point(0, 0)
    p2 = Point(2, 0)
    p3 = Point(0, 2)
    c1 = ShapeFactory.build("circle", p1, p2, p3)
    c1.draw(graphics)
    graphics.show()

def drawComposite(graphics):
    center = Point(0, 0)
    r1 = ShapeFactory.build("rectangle", Point(1, 1), Point(4, 1), Point(4, 3), Point(1, 3))
    t1 = ShapeFactory.build("triangle", Point(1, 2), Point(5, 1), Point(3, 3))
    c1 = ShapeFactory.build("circle", Point(0, 0), Point(2, 0), Point(0, 2))
    e1 = ShapeFactory.build("ellipse", Point(0, 0), Point(3, 0), Point(0, 2))
    cm1 = ShapeFactory.build("composite", center, r1)
    cm2 = ShapeFactory.build("composite", center, t1, c1)
    cm3 = ShapeFactory.build("composite", center, cm1, e1, cm2)
    cm3.draw(graphics)
    graphics.show()


setupGraphics()
drawLine(graphics)
drawTriangle(graphics)
drawRectangle(graphics)
drawSquare(graphics)
drawEllipse(graphics)
drawCircle(graphics)
drawComposite(graphics)
