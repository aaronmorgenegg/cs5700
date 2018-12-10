from sudoku_solver.constants import BLANK_CELL, VERBOSITY
from sudoku_solver.coordinates import Coordinates
from sudoku_solver.strategies.hidden_single import HiddenSingle
from sudoku_solver.strategies.naked_pair import NakedPair
from sudoku_solver.strategies.single_possibility import SinglePossibility
from sudoku_solver.strategies.strategy import Strategy
from sudoku_solver.sudoku_board import SudokuBoard
from sudoku_solver.sudoku_board_exception import SudokuBoardException
from sudoku_solver.timer import Timer


class SudokuSolver:
    def __init__(self, sudoku_board):
        self.sudoku_board = sudoku_board
        self.solve_strategies = [SinglePossibility(), HiddenSingle()]
        self.choices_strategies = [NakedPair()]
        self.time = {'total': 0, 'computing_choices': 0, 'choosing_strategy': 0, 'applying_strategy': 0}
        self.timer = Timer()
        self.history = []

    def solvePuzzle(self):
        self.timer.startTimer()

        self.history.append({'type': 'startSolvePuzzle'})
        try:
            self.sudoku_board.validate()
        except SudokuBoardException as e:
            self.time['total'] += self.timer.stopTimer()
            return self._invalidSolutionToString(e)

        return self.tryStrategies()

    def tryStrategies(self):
        while self.sudoku_board.num_blank_cells > 0:
            self.tryStrategy()

        try:
            self.sudoku_board.validate()
        except SudokuBoardException as e:
            self.time['total'] += self.timer.stopTimer()
            return self._invalidSolutionToString("Puzzle could not be solved.\n"+str(e))

        self.history.append({'type': 'solvePuzzle'})
        self.time['total'] += self.timer.stopTimer()
        return self._solutionToString()

    def tryStrategy(self):
        choices, choices_time = Timer.timeFunction(self._updateChoicesArray)
        self.time['computing_choices'] += choices_time
        strategy, choosing_time = Timer.timeFunction(self._findAppropriateSolveStrategy, choices)
        self.time['choosing_strategy'] += choosing_time
        if strategy is None:
            # This means none of the strategies worked
            self.time['total'] += self.timer.stopTimer()
            return self._invalidSolutionToString("No strategy could be found to solve this puzzle")

        change, apply_time = Timer.timeFunction(strategy.invoke, self.sudoku_board, choices)
        if change is not None:
            self.history.append(change)
        self.time['applying_strategy'] += apply_time

    def undo(self):
        change = self.history.pop()
        if change['type'] == 'solvePuzzle':
            self._undoSolvePuzzle()
        else:
            self._undoSetCell(change)

    def _undoSetCell(self, change):
        Strategy.undo(self.sudoku_board, change)

    def _undoSolvePuzzle(self):
        for i in range(len(self.history)):
            change = self.history.pop()
            if change['type'] == 'startSolvePuzzle':
                return
            self._undoSetCell(change)

    def _updateChoicesArray(self):
        choices=[]
        for row_x, row in enumerate(self.sudoku_board.rows):
            choices.append([])
            for row_y, cell in enumerate(row):
                if self.sudoku_board.rows[row_x][row_y] == BLANK_CELL:
                    choices[row_x].append(self._findChoices(self.sudoku_board, row_x, row_y))
                else:
                    choices[row_x].append([])
        self._applyChoicesStrategies(choices)
        return choices

    def _applyChoicesStrategies(self, choices):
        for strategy in self.choices_strategies:
            if VERBOSITY > 2: print("Applying {} strategy".format(type(strategy).__name__))
            strategy.invoke(self.sudoku_board, choices)

    def _findChoices(self, sudoku_board, row_x, row_y):
        col_x, col_y = Coordinates.convert(row_x, row_y, "column", sudoku_board.size)
        block_x, block_y = Coordinates.convert(row_x, row_y, "block", sudoku_board.size)
        row_choices = list(set(sudoku_board.valid_symbols) - set(sudoku_board.rows[row_x])-set(BLANK_CELL))
        col_choices = list(set(sudoku_board.valid_symbols) - set(sudoku_board.columns[col_x])-set(BLANK_CELL))
        block_choices = list(set(sudoku_board.valid_symbols) - set(sudoku_board.blocks[block_x])-set(BLANK_CELL))

        choice = [choice for choice in row_choices if choice in col_choices]
        choice = [choice for choice in choice if choice in block_choices]

        return choice

    def _findAppropriateSolveStrategy(self, choices):
        for strategy in self.solve_strategies:
            if strategy.isAppropriate(self.sudoku_board, choices):
                if VERBOSITY > 2: print("Applying {} strategy".format(type(strategy).__name__))
                return strategy
        return None

    def _invalidSolutionToString(self, error):
        return self._solutionToString() + "\n\nCould not be solved: " + str(error)

    def _solutionToString(self):
        string = self.sudoku_board.toString()
        string += "="*((2*self.sudoku_board.size)-1)
        string += SudokuBoard.boardToString(self.sudoku_board.rows)
        string += self._timeToString()
        return string

    def _timeToString(self):
        string = "\nTotal time                : " + Timer.prettyPrintTime(self.time['total'])
        string += "\nComputing Choices time    : " + Timer.prettyPrintTime((self.time['computing_choices']))
        string += "\nChoosing Strategies time  : " + Timer.prettyPrintTime((self.time['choosing_strategy']))
        string += "\nApplying Strategies time  : " + Timer.prettyPrintTime((self.time['applying_strategy']))
        string += "\nStrategies:"
        for seq in (self.choices_strategies, self.solve_strategies):
            for strategy in seq:
                string += "\n{}".format(type(strategy).__name__)
                string += "\n   Number of times used   : {}".format(strategy.num_usages)
                string += "\n   Choosing Strategy Time : {}".format(Timer.prettyPrintTime(strategy.choosing_time))
                string += "\n   Applying Strategy Time : {}".format(Timer.prettyPrintTime(strategy.applying_time))
        return string

    def toString(self):
        if self.sudoku_board.num_blank_cells == 0:
            return self._solutionToString()
        else:
            return self._invalidSolutionToString("Board saved before being completely solved")
