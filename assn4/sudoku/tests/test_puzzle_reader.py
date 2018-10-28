import unittest

from sudoku_solver.PuzzleReader import PuzzleReader


class TestPuzzleReader(unittest.TestCase):
    def testReadFromFile(self):
        test_reader = PuzzleReader()
        filename = "test_puzzles/input/Puzzle-9x9-0001.txt"
        SudokuBoard = test_reader.readPuzzle(filename)
        self.assertEqual(SudokuBoard.size, 9)
        self.assertEqual(SudokuBoard.valid_symbols, ['1','2','3','4','5','6','7','8','9'])