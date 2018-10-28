from sudoku_solver import sudoku_board_exception
from sudoku_solver.timer import Timer


class SudokuSolver:
    def __init__(self, sudoku_board):
        self.sudoku_board = sudoku_board
        self.timer = Timer()

    def solve(self):
        self.timer.startTimer()
        
        try:
            self.sudoku_board.validate()
        except sudoku_board_exception as e:
            return self.sudoku_board.toString() + "\n" + e

        return self.toString()

    def toString(self):
        return self.sudoku_board.toString()
