import copy
import math

from sudoku_solver.constants import BLANK_CELL, VALID_SIZES
from sudoku_solver.coordinates import Coordinates
from sudoku_solver.sudoku_board_exception import SudokuBoardException


class SudokuBoard:
    def __init__(self, size, valid_symbols, initial_board):
        self.size = size
        self.valid_symbols = valid_symbols
        self.initial_board = initial_board
        self.rows = copy.deepcopy(initial_board)
        self._initCols()
        self._initBlocks()
        self._initBlanks()

    def _initCols(self):
        self.columns = []
        try:
            for i in range(self.size):
                self.columns.append([x[i] for x in self.rows])
        except IndexError:
            raise SudokuBoardException

    def _initBlocks(self):
        self.blocks = []
        block_size = int(math.sqrt(self.size))
        try:
            for i in range(self.size):
                block = []
                for j in range(block_size):
                    for k in range(block_size):
                        row = j+(i//block_size)*block_size
                        col = k+(i*block_size)%self.size
                        block.append(self.rows[row][col])
                self.blocks.append(block)
        except IndexError:
            raise SudokuBoardException

    def _initBlanks(self):
        self.num_blank_cells = 0
        for row in self.rows:
            for cell in row:
                if cell == BLANK_CELL:
                    self.num_blank_cells += 1

    def getCell(self, row, col):
        return self.rows[row][col]

    def setCell(self, row, col, value):
        """Set given cell to value"""
        if value not in self.valid_symbols and value != BLANK_CELL:
            raise SudokuBoardException("Error: Attempting to set cell to non-valid symbol")
        try:
            old_cell = self.getCell(row, col)
            self._setRowCell(row, col, value)
            self._setColumnCell(row, col, value)
            self._setBlockCell(row, col, value)
            if old_cell == BLANK_CELL and value != BLANK_CELL:
                self.num_blank_cells -= 1
            elif old_cell != BLANK_CELL and value == BLANK_CELL:
                self.num_blank_cells += 1
        except IndexError:
            print("Error: setCell({},{},{}) out of bounds".format(row, col, value))

    def _setRowCell(self, row, col, value):
        x, y = Coordinates.convert(row, col, "row", size=self.size)
        self.rows[x][y] = value

    def _setColumnCell(self, row, col, value):
        x, y = Coordinates.convert(row, col, "column", size=self.size)
        self.columns[x][y] = value

    def _setBlockCell(self, row, col, value):
        x, y = Coordinates.convert(row, col, "block", size=self.size)
        self.blocks[x][y] = value

    def toString(self):
        string = ""
        string += str(self.size) + "\n"
        for symbol in self.valid_symbols:
            string += str(symbol) + " "
        string += SudokuBoard.boardToString(self.initial_board)
        return string

    @staticmethod
    def boardToString(board):
        """Print a board/2d array to a string"""
        string = "\n"
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
        if len(self.valid_symbols) > len(set(self.valid_symbols)):
            raise SudokuBoardException("One or more symbols are not unique")
        for symbol in self.valid_symbols:
            if symbol == BLANK_CELL:
                raise SudokuBoardException("Symbol cannot be the same as a blank cell ({})".format(BLANK_CELL))

    def _validateBoard(self):
        if type(self.rows) != list:
            raise SudokuBoardException("Board list error")
        if len(self.rows) != self.size:
            raise SudokuBoardException("Not enough rows for sudoku board")
        if len(self.columns) != self.size:
            raise SudokuBoardException("Not enough columns for sudoku board")
        for row in self.rows:
            if type(row) != list:
                raise SudokuBoardException("Board row list error")
            if len(row) != self.size:
                raise SudokuBoardException("Not enough cells in row for sudoku board")
            found_cells = []
            for cell in row:
                if cell in found_cells and self.num_blank_cells == 0:
                    raise SudokuBoardException("Multiple of symbol ({}) found in row".format(cell))
                found_cells.append(cell)
                if cell not in self.valid_symbols and cell != BLANK_CELL:
                    raise SudokuBoardException("Invalid symbol ({}) for cell".format(cell))
        for col in self.columns:
            found_cells = []
            for cell in col:
                if cell in found_cells and self.num_blank_cells == 0:
                    raise SudokuBoardException("Multiple of symbol ({}) found in column".format(cell))
                found_cells.append(cell)
        for block in self.blocks:
            found_cells = []
            for cell in block:
                if cell in found_cells and self.num_blank_cells == 0:
                    raise SudokuBoardException("Multiple of symbol ({}) found in block".format(cell))
                found_cells.append(cell)
