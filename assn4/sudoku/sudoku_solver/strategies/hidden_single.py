from sudoku_solver.constants import BLANK_CELL
from sudoku_solver.coordinates import Coordinates
from sudoku_solver.strategies.strategy import Strategy


class HiddenSingle(Strategy):
    def _findChanges(self, sudoku_board):
        choices = self._findChoices(sudoku_board)
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

    def _findChoices(self, sudoku_board):
        choices=[]
        for row_x, row in enumerate(sudoku_board.rows):
            choices.append([])
            for row_y, cell in enumerate(row):
                if sudoku_board.rows[row_x][row_y] == BLANK_CELL:
                    choices[row_x].append(self._findChoice(sudoku_board, row_x, row_y))
                else:
                    choices[row_x].append([])
        return choices

    def _findChoice(self, sudoku_board, row_x, row_y):
        col_x, col_y = Coordinates.convert(row_x, row_y, "column", sudoku_board.size)
        block_x, block_y = Coordinates.convert(row_x, row_y, "block", sudoku_board.size)
        row_choices = list(set(sudoku_board.valid_symbols) - set(sudoku_board.rows[row_x])-set(BLANK_CELL))
        col_choices = list(set(sudoku_board.valid_symbols) - set(sudoku_board.columns[col_x])-set(BLANK_CELL))
        block_choices = list(set(sudoku_board.valid_symbols) - set(sudoku_board.blocks[block_x])-set(BLANK_CELL))

        choice = [choice for choice in row_choices if choice in col_choices]
        choice = [choice for choice in choice if choice in block_choices]

        return choice
