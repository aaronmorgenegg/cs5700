import unittest
import time

from sudoku_solver.timer import Timer


class TestTimer(unittest.TestCase):
    def testStartTimer(self):
        timer = Timer()
        timer.startTimer()
        expected = 0.01
        time.sleep(expected)
        actual = timer.stopTimer()
        self.assertAlmostEqual(expected, actual, places=2)

    def testPrettyPrintTime(self):
        expected = "0.00014s"
        actual = Timer.prettyPrintTime(0.00014134995)
        self.assertEqual(expected, actual)

    def testTimeFunction(self):
        expected = 0.01
        _, actual = Timer.timeFunction(time.sleep, expected)
        self.assertAlmostEqual(expected, actual, places=2)
