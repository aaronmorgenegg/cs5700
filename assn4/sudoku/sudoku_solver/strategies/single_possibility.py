from sudoku_solver.constants import BLANK_CELL
from sudoku_solver.coordinates import Coordinates
from sudoku_solver.strategies.strategy import Strategy


class SinglePossibility(Strategy):
    """If there is only 1 possibility for a cell in a given row/column/block"""
    def _findChanges(self, sudoku_board):
        for row_x, row in enumerate(sudoku_board.rows):
            for row_y, cell in enumerate(row):
                if sudoku_board.rows[row_x][row_y] == BLANK_CELL:
                    choices = self._findChoices(sudoku_board, row_x, row_y)
                    if len(choices) == 1:
                        return {'row': row_x, 'column': row_y, 'cell': choices[0]}
        return {}

    def _findChoices(self, sudoku_board, row_x, row_y):
        col_x, col_y = Coordinates.convert(row_x, row_y, "column", sudoku_board.size)
        block_x, block_y = Coordinates.convert(row_x, row_y, "block", sudoku_board.size)
        row_choices = list(set(sudoku_board.valid_symbols)-set(sudoku_board.rows[row_x])-set(BLANK_CELL))
        col_choices = list(set(sudoku_board.valid_symbols) - set(sudoku_board.columns[col_x])-set(BLANK_CELL))
        block_choices = list(set(sudoku_board.valid_symbols) - set(sudoku_board.blocks[block_x])-set(BLANK_CELL))

        choices = [choice for choice in row_choices if choice in col_choices]
        choices = [choice for choice in choices if choice in block_choices]

        return choices
