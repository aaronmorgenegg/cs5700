import unittest
import time

from sudoku_solver.timer import Timer


class TestTimer(unittest.TestCase):
    def testStartTimer(self):
        timer = Timer()
        timer.startTimer()
        expected = 0.1
        time.sleep(expected)
        actual = timer.stopTimer()
        self.assertAlmostEqual(expected, actual, places=3)

    def testPrettyPrintTime(self):
        expected = "0.00014s"
        actual = Timer.prettyPrintTime(0.00014134995)
        self.assertEqual(expected, actual)
