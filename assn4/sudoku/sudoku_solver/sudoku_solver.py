from sudoku_solver.strategies.only_choice import OnlyChoice
from sudoku_solver.strategies.single_possibility import SinglePossibility
from sudoku_solver.sudoku_board import SudokuBoard
from sudoku_solver.sudoku_board_exception import SudokuBoardException
from sudoku_solver.timer import Timer


class SudokuSolver:
    def __init__(self, sudoku_board):
        self.sudoku_board = sudoku_board
        self.strategies = [OnlyChoice(), SinglePossibility()]
        self.time = {'total': 0, 'choosing_strategy': 0, 'applying_strategy': 0}
        self.timer = Timer()

    def solvePuzzle(self):
        self.timer.startTimer()

        try:
            self.sudoku_board.validate()
        except SudokuBoardException as e:
            return self._invalidSolutionToString(e)

        return self._tryStrategies()

    def _tryStrategies(self):
        while self.sudoku_board.num_blank_cells > 0:
            strategy, choosing_time = self.timer.timeFunction(self._findAppropriateStrategy())
            if strategy is None:
                # This means none of the strategies worked
                return self._invalidSolutionToString("No strategy could be found to solve this puzzle")

            self.time['choosing_strategy'] += choosing_time
            _, apply_time = self.timer.timeFunction(strategy.invoke, self.sudoku_board)
            self.time['applying_strategy'] += apply_time

        try:
            self.sudoku_board.validate()
        except SudokuBoardException as e:
            return self._invalidSolutionToString("Puzzle could not be solved.\n"+str(e))

        self.time['total'] += self.timer.stopTimer()
        return self._solutionToString()

    def _findAppropriateStrategy(self):
        for strategy in self.strategies:
            if strategy.isAppropriate(self.sudoku_board):
                return strategy
        return None

    def _invalidSolutionToString(self, error):
        return self.sudoku_board.toString() + "\n" + str(error)

    def _solutionToString(self):
        string = self.sudoku_board.toString()
        string += "="*((2*self.sudoku_board.size)-1)
        string += SudokuBoard.boardToString(self.sudoku_board.rows)
        string += "\nTotal time               : " + Timer.prettyPrintTime(self.time['total'])
        string += "\nChoosing Strategies time : " + Timer.prettyPrintTime((self.time['choosing_strategy']))
        string += "\nApplying Strategies time : " + Timer.prettyPrintTime((self.time['applying_strategy']))
        string += self._strategiesToString()
        return string

    def _strategiesToString(self):
        string = "\nStrategies:"
        for strategy in self.strategies:
            string += "\n{}".format(type(strategy).__name__)
            string += "\n   Number of times used  : {}".format(strategy.num_usages)
            string += "\n   Choosing Strategy Time: {}".format(Timer.prettyPrintTime(strategy.choosing_time))
            string += "\n   Applying Strategy Time: {}".format(Timer.prettyPrintTime(strategy.applying_time))
        return string
