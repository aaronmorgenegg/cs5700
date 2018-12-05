from sudoku_solver.strategies.strategy import Strategy


class NakedPair(Strategy):
    def __init__(self):
        super().__init__()
        self.type = "choice"

    def _findChanges(self, sudoku_board, choices):
        for row_x, row in enumerate(choices):
            for row_y, choice_list in enumerate(row):
                if len(choice_list) == 2:
                    self._checkRows(row_x, row_y, choices, choice_list)
                    self._checkColumns(row_x, row_y, choices, choice_list)
                    # self._checkBlocks(row_x, row_y, choices, choice_list)
        return {}

    def _checkRows(self, row_x, row_y, choices, choice_list):
        size = len(choices)
        for i in range(size):
            if choice_list == choices[row_x][i] and i != row_y:
                # found a naked pair
                for j in range(size):
                    if j != row_y and j != i:
                        for choice in choice_list:
                            try:
                                choices[row_x][j].remove(choice)
                            except ValueError:
                                pass
        return {}

    def _checkColumns(self, row_x, row_y, choices, choice_list):
        size = len(choices)
        for i in range(size):
            if choice_list == choices[i][row_y] and i != row_x:
                # found a naked pair
                for j in range(size):
                    if j != row_x and j != i:
                        for choice in choice_list:
                            try:
                                choices[j][row_y].remove(choice)
                            except ValueError:
                                pass
        return {}
