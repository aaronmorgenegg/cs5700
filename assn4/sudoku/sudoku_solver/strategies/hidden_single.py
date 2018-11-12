from sudoku_solver.coordinates import Coordinates
from sudoku_solver.strategies.strategy import Strategy


class HiddenSingle(Strategy):
    def __init__(self):
        super().__init__()
        self.type = "solve"

    def _findChanges(self, sudoku_board, choices):
        for row_x, row in enumerate(choices):
            for row_y, choice_list in enumerate(row):
                for choice in choice_list:
                    # if choice not in row_choices, col_choices, or block_choices
                    if self._checkSingleRow(choices, choice, row_x, sudoku_board.size) and  \
                       self._checkSingleColumn(choices, choice, row_y, sudoku_board.size) and \
                       self._checkSingleBlock(choices, choice, row_x, row_y, sudoku_board.size):
                        return {'row': row_x, 'column': row_y, 'cell': choice}
        return {}

    def _checkSingleRow(self, choices, choice, row, size):
        count = 0
        for i in range(size):
            if choice in choices[row][i]:
                count += 1
            if count > 1: return False
        return count == 1

    def _checkSingleColumn(self, choices, choice, column, size):
        count = 0
        for i in range(size):
            if choice in choices[i][column]:
                count += 1
            if count > 1: return False
        return count == 1

    def _checkSingleBlock(self, choices, choice, row_x, row_y, size):
        count = 0
        block = Coordinates.convert(row_x, row_y, "block", size)
        for x, row in enumerate(choices):
            for y, choice_list in enumerate(row):
                iter_block = Coordinates.convert(x, y, "block", size)
                if block == iter_block:
                    if choice in choices[x][y]:
                        count += 1
                    if count > 1: return False
        return count == 1
