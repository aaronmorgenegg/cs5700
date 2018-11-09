from sudoku_solver.strategies.only_choice import OnlyChoice
from sudoku_solver.sudoku_board_exception import SudokuBoardException
from sudoku_solver.timer import Timer


class SudokuSolver:
    def __init__(self, sudoku_board):
        self.sudoku_board = sudoku_board
        self.timer = Timer()

    def solvePuzzle(self):
        self.timer.startTimer()

        try:
            self.sudoku_board.validate()
        except SudokuBoardException as e:
            return self._invalidSolutionToString(e)

        # TODO: implement strategies to solve sudoku puzzle
        max_iter = 100
        while self.sudoku_board.num_blank_cells > 0 and max_iter >= 0:
            strategy = OnlyChoice()
            strategy.invoke(self.sudoku_board)
            max_iter -= 1
            if max_iter == 0:
                print("Max iterations achieved")

        return self._solutionToString()

    def _invalidSolutionToString(self, error):
        return self.sudoku_board.toString() + "\n" + str(error)

    def _solutionToString(self):
        string = self.sudoku_board.toString()
        string += "\nTotal time: " + str(self.timer.stopTimer())
        return string
