from sudoku_solver.constants import BLANK_CELL
from sudoku_solver.coordinates import Coordinates
from sudoku_solver.strategies.strategy import Strategy


class OnlyChoice(Strategy):
    def _applyChanges(self, sudoku_board, coords):
        if len(coords) == 0: return
        self._insertMissingCell(sudoku_board, coords)

    def _findCoords(self, sudoku_board):
        for index, row in enumerate(sudoku_board.rows):
            if row.count(BLANK_CELL) == 1:
                x, y = Coordinates.convert(index, row.index(BLANK_CELL), "row")
                return {'row': x, 'column': y}
        for index, col in enumerate(sudoku_board.columns):
            if col.count(BLANK_CELL) == 1:
                x, y = Coordinates.convert(index, col.index(BLANK_CELL), "column")
                return {'row': x, 'column': y}
        for index, block in enumerate(sudoku_board.blocks):
            if block.count(BLANK_CELL) == 1:
                x, y = Coordinates.convert(index, block.index(BLANK_CELL), "block")
                return {'row': x, 'column': y}
        return {}

    def _insertMissingCell(self, sudoku_board, coordinates):
        missing_cell = list(set(sudoku_board.valid_symbols) - set(sudoku_board.rows[coordinates['row']]))[0]
        sudoku_board.setCell(coordinates['row'], coordinates['column'], missing_cell)
