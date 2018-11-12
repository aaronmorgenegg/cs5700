import unittest

from sudoku_solver.sudoku_board import SudokuBoard
from sudoku_solver.sudoku_solver import SudokuSolver


class TestSudokuSolver(unittest.TestCase):
    def testSolvePuzzle(self):
        size = 4
        valid_symbols = ['1','2','3','4']
        initial_board = [['2', '-', '3', '1'],
                         ['1', '3', '-', '4'],
                         ['3', '1', '4', '-'],
                         ['-', '2', '1', '3']]
        sudoku_board = SudokuBoard(size, valid_symbols, initial_board)
        sudoku_solver = SudokuSolver(sudoku_board)
        sudoku_solver.solvePuzzle()
        actual = sudoku_solver.sudoku_board
        expected_board = [['2', '4', '3', '1'],
                         ['1', '3', '2', '4'],
                         ['3', '1', '4', '2'],
                         ['4', '2', '1', '3']]
        expected = SudokuBoard(size, valid_symbols, expected_board)
        self.assertEqual(actual.rows, expected.rows)
        self.assertEqual(actual.columns, expected.columns)
        self.assertEqual(actual.blocks, expected.blocks)
        self.assertEqual(actual.num_blank_cells, expected.num_blank_cells)