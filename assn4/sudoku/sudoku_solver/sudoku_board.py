from sudoku_solver.constants import BLANK_CELL, VALID_SIZES
from sudoku_solver.sudoku_board_exception import SudokuBoardException


class SudokuBoard:
    def __init__(self, size, valid_symbols, initial_board):
        self.size = size
        self.valid_symbols = valid_symbols
        self.initial_board = initial_board
        self.current_board = initial_board

    def toString(self):
        string = ""
        string += str(self.size) + "\n"
        for symbol in self.valid_symbols:
            string += str(symbol) + " "
        string += "\n"
        string += self.boardToString(self.initial_board)
        return string

    def boardToString(self, board):
        string = ""
        for row in board:
            for cell in row:
                string += cell + " "
            string += "\n"
        return string

    def validate(self):
        self._validateSize()
        self._validateSymbols()
        self._validateBoard()

    def _validateSize(self):
        if type(self.size) != int:
            raise SudokuBoardException("Size is an invalid integer")
        if self.size not in VALID_SIZES:
            raise SudokuBoardException("Sudoku Solver cannot handle board of size ({})".format(self.size))

    def _validateSymbols(self):
        if type(self.valid_symbols) != list:
            raise SudokuBoardException("Valid symbol list error")
        if len(self.valid_symbols) != self.size:
            raise SudokuBoardException("Valid symbol list does not match board size")
        if len(self.valid_symbols > len(set(self.valid_symbols))):
            raise SudokuBoardException("One or more symbols are not unique")
        for symbol in self.valid_symbols:
            if symbol == BLANK_CELL:
                raise SudokuBoardException("Symbol cannot be the same as a blank cell ({})".format(BLANK_CELL))

    def _validateBoard(self):
        if type(self.current_board) != list:
            raise SudokuBoardException("Board list error")
        if len(self.current_board) != self.size:
            raise SudokuBoardException("Not enough rows for sudoku board")
        for row in self.current_board:
            if type(row) != list:
                raise SudokuBoardException("Board row list error")
            if len(row) != self.size:
                raise SudokuBoardException("Not enough cells in row for sudoku board")
            for cell in row:
                if cell not in self.valid_symbols or cell != BLANK_CELL:
                    raise SudokuBoardException("Invalid symbol for cell ({})".format(cell))
