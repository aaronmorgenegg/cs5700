from sudoku_solver.strategies.only_choice import OnlyChoice
from sudoku_solver.sudoku_board_exception import SudokuBoardException
from sudoku_solver.timer import Timer


class SudokuSolver:
    def __init__(self, sudoku_board):
        self.sudoku_board = sudoku_board
        self.strategies = [OnlyChoice()]
        self.time = {'total': 0, 'choosing_strategy': 0, 'applying_strategy': 0}

    def solvePuzzle(self):
        total_timer = Timer()
        total_timer.startTimer()

        try:
            self.sudoku_board.validate()
        except SudokuBoardException as e:
            return self._invalidSolutionToString(e)

        while self.sudoku_board.num_blank_cells > 0:
            solve_timer = Timer()
            solve_timer.startTimer()
            for strategy in self.strategies:
                if strategy.isAppropriate(self.sudoku_board):
                    self.time['choosing_strategy'] += solve_timer.stopTimer()
                    solve_timer.startTimer()
                    strategy.invoke(self.sudoku_board)
                    self.time['applying_strategy'] += solve_timer.stopTimer()
                    break
            # This means none of the strategies worked
            return self._invalidSolutionToString("No strategy could be found to solve this puzzle")

        self.time['total'] += total_timer.stopTimer()
        return self._solutionToString()

    def _invalidSolutionToString(self, error):
        return self.sudoku_board.toString() + "\n" + str(error)

    def _solutionToString(self):
        string = self.sudoku_board.toString()
        string += "\nTotal time               : " + str(self.time['total'])
        string += "\nChoosing Strategies time : " + str(self.time['choosing_strategy'])
        string += "\nApplying Strategies time : " + str(self.time['applying_strategy'])
        return string
