import unittest

from sudoku_solver.coordinates import Coordinates


class TestCoordinates(unittest.TestCase):
    def testConvertBlock(self):
        x1 = 0
        y1 = 0
        x1, y1 = Coordinates.convert(x1, y1, "block", 9)
        self.assertEqual(x1, 0)
        self.assertEqual(y1, 0)

        x2 = 2
        y2 = 2
        x2, y2 = Coordinates.convert(x2, y2, "block", 9)
        self.assertEqual(x2, 0)
        self.assertEqual(y2, 8)

        x3 = 4
        y3 = 7
        x3, y3 = Coordinates.convert(x3, y3, "block", 9)
        self.assertEqual(x3, 5)
        self.assertEqual(y3, 4)

        x3 = 2
        y3 = 6
        x3, y3 = Coordinates.convert(x3, y3, "block", 9)
        self.assertEqual(x3, 2)
        self.assertEqual(y3, 6)
