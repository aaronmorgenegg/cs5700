import unittest

from sudoku_solver.sudoku_board import SudokuBoard


class TestSudokuBoard(unittest.TestCase):
    def testConstruction(self):
        size = 9
        valid_symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        initial_board = [['-', '-', '-', '6', '4', '-', '-', '-', '-'],
                         ['-', '3', '-', '-', '7', '9', '-', '6', '8'],
                         ['-', '8', '-', '-', '-', '-', '-', '-', '1'],
                         ['9', '-', '-', '-', '2', '6', '-', '5', '3'],
                         ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                         ['6', '5', '-', '8', '3', '-', '-', '-', '2'],
                         ['8', '-', '-', '-', '-', '-', '-', '3', '-'],
                         ['3', '6', '-', '7', '8', '-', '-', '4', '-'],
                         ['-', '-', '-', '-', '6', '1', '-', '-', '-']
                        ]
        sudoku_board1 = SudokuBoard(size, valid_symbols, initial_board)
        expected_rows = initial_board
        expected_cols = [['-', '-', '-', '9', '-', '6', '8', '3', '-'],
                         ['-', '3', '8', '-', '-', '5', '-', '6', '-'],
                         ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                         ['6', '-', '-', '-', '-', '8', '-', '7', '-'],
                         ['4', '7', '-', '2', '-', '3', '-', '8', '6'],
                         ['-', '9', '-', '6', '-', '-', '-', '-', '1'],
                         ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                         ['-', '6', '-', '5', '-', '-', '3', '4', '-'],
                         ['-', '8', '1', '3', '-', '2', '-', '-', '-']
                        ]
        expected_blocks = [['-', '-', '-', '-', '3', '-', '-', '8', '-'],
                           ['6', '4', '-', '-', '7', '9', '-', '-', '-'],
                           ['-', '-', '-', '-', '6', '8', '-', '-', '1'],
                           ['9', '-', '-', '-', '-', '-', '6', '5', '-'],
                           ['-', '2', '6', '-', '-', '-', '8', '3', '-'],
                           ['-', '5', '3', '-', '-', '-', '-', '-', '2'],
                           ['8', '-', '-', '3', '6', '-', '-', '-', '-'],
                           ['-', '-', '-', '7', '8', '-', '-', '6', '1'],
                           ['-', '3', '-', '-', '4', '-', '-', '-', '-']
                          ]
        self.assertEqual(size, sudoku_board1.size)
        self.assertEqual(valid_symbols, sudoku_board1.valid_symbols)
        self.assertEqual(expected_rows, sudoku_board1.rows)
        self.assertEqual(expected_cols, sudoku_board1.columns)
        self.assertEqual(expected_blocks, sudoku_board1.blocks)

    def testSetCell(self):
        size = 9
        valid_symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        initial_board = [['-', '-', '-', '6', '4', '-', '-', '-', '-'],
                         ['-', '3', '-', '-', '7', '9', '-', '6', '8'],
                         ['-', '8', '-', '-', '-', '-', '-', '-', '1'],
                         ['9', '-', '-', '-', '2', '6', '-', '5', '3'],
                         ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
                         ['6', '5', '-', '8', '3', '-', '-', '-', '2'],
                         ['8', '-', '-', '-', '-', '-', '-', '3', '-'],
                         ['3', '6', '-', '7', '8', '-', '-', '4', '-'],
                         ['-', '-', '-', '-', '6', '1', '-', '-', '-']
                        ]
        sudoku_board1 = SudokuBoard(size, valid_symbols, initial_board)
        sudoku_board1.setCell(0, 1, '7')
        self.assertEqual('7', sudoku_board1.rows[0][1])
        self.assertEqual('7', sudoku_board1.columns[1][0])
        self.assertEqual('7', sudoku_board1.blocks[0][1])

        sudoku_board1.setCell(0, 7, '1')
        self.assertEqual('1', sudoku_board1.rows[0][7])
        self.assertEqual('1', sudoku_board1.columns[7][0])
        self.assertEqual('1', sudoku_board1.blocks[2][1])

        sudoku_board1.setCell(3, 2, '4')
        self.assertEqual('4', sudoku_board1.rows[3][2])
        self.assertEqual('4', sudoku_board1.columns[2][3])
        self.assertEqual('4', sudoku_board1.blocks[3][2])

        sudoku_board1.setCell(4, 4, '9')
        self.assertEqual('9', sudoku_board1.rows[4][4])
        self.assertEqual('9', sudoku_board1.columns[4][4])
        self.assertEqual('9', sudoku_board1.blocks[4][4])

        sudoku_board1.setCell(7, 6, '2')
        self.assertEqual('2', sudoku_board1.rows[7][6])
        self.assertEqual('2', sudoku_board1.columns[6][7])
        self.assertEqual('2', sudoku_board1.blocks[8][3])
