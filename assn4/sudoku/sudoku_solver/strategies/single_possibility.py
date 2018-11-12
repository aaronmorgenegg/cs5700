from sudoku_solver.constants import BLANK_CELL
from sudoku_solver.strategies.strategy import Strategy


class SinglePossibility(Strategy):
    """If there is only 1 possibility for a cell in a given row/column/block"""
    def _findChanges(self, sudoku_board, choices):
        for row_x, row in enumerate(sudoku_board.rows):
            for row_y, cell in enumerate(row):
                if sudoku_board.rows[row_x][row_y] == BLANK_CELL:
                    choice_list = choices[row_x][row_y]
                    if len(choice_list) == 1:
                        return {'row': row_x, 'column': row_y, 'cell': choice_list[0]}
        return {}
