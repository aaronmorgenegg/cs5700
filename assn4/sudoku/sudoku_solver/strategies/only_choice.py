from sudoku_solver.constants import BLANK_CELL
from sudoku_solver.coordinates import Coordinates
from sudoku_solver.strategies.strategy import Strategy


class OnlyChoice(Strategy):
    """If there is only 1 blank cell in a row, column, or block"""
    def _findChanges(self, sudoku_board):
        for index, row in enumerate(sudoku_board.rows):
            if row.count(BLANK_CELL) == 1:
                return self._getChanges(index, row.index(BLANK_CELL), "row", sudoku_board)
        for index, col in enumerate(sudoku_board.columns):
            if col.count(BLANK_CELL) == 1:
                return self._getChanges(index, col.index(BLANK_CELL), "column", sudoku_board)
        for index, block in enumerate(sudoku_board.blocks):
            if block.count(BLANK_CELL) == 1:
                return self._getChanges(index, block.index(BLANK_CELL), "block", sudoku_board)
        return {}

    def _getChanges(self, index, blank_cell_index, mode, sudoku_board):
        x, y = Coordinates.convert(index, blank_cell_index, mode, sudoku_board.size)
        missing_cell = list(set(sudoku_board.valid_symbols) - set(sudoku_board.rows[x]))[0]
        return {'row': x, 'column': y, 'cell': missing_cell}
