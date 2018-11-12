import unittest

from sudoku_solver.puzzle_reader import PuzzleReader


class TestPuzzleReader(unittest.TestCase):
    def testReadFromFile(self):
        test_reader = PuzzleReader()
        filename = "test_puzzles/test_input/Puzzle-9x9-0001.txt"
        sudoku_board = test_reader.loadPuzzle(filename)
        self.assertEqual(sudoku_board.size, 9)
        self.assertEqual(sudoku_board.valid_symbols, ['1','2','3','4','5','6','7','8','9'])

    def testReadFromFileBadPuzzle(self):
        test_reader = PuzzleReader()
        filename = "test_puzzles/test_input/Puzzle-4x4-0905.txt"
        sudoku_board = test_reader.loadPuzzle(filename)
        self.assertEqual(type(sudoku_board), str)
        self.assertEqual(sudoku_board, "4\nA B C D\nB D C A\nA C B D\n\nBad Puzzle")
