from sudoku_solver.constants import BLANK_CELL
from sudoku_solver.strategies.strategy import Strategy


class OnlyChoice(Strategy):
    def _applyChanges(self, sudoku_board):
        for row in sudoku_board.rows:
            if row.count(BLANK_CELL) == 1:
                self._insertMissingCell(sudoku_board, row)
        for col in sudoku_board.columns:
            if col.count(BLANK_CELL) == 1:
                return True
        for block in sudoku_board.blocks:
            if block.count(BLANK_CELL) == 1:
                return True
        return False

    def _findCoords(self, sudoku_board):
        for index, row in enumerate(sudoku_board.rows):
            if row.count(BLANK_CELL) == 1:
                return {'row': index, 'column': row.index(BLANK_CELL)}
        for index, col in enumerate(sudoku_board.columns):
            if col.count(BLANK_CELL) == 1:
                return {'row': col.index(BLANK_CELL), 'column': index}
        for index, block in enumerate(sudoku_board.blocks):
            if block.count(BLANK_CELL) == 1:
                return {'row': index, 'column': block.index(BLANK_CELL)}
        return {}

    def _insertMissingCell(self, sudoku_board, row):
        missing_cell = list(set(sudoku_board.valid_symbols) - set(row))[0]
        sudoku_board.setCell(row, row.index(BLANK_CELL), missing_cell)
