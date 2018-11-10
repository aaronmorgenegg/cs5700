from sudoku_solver.timer import Timer


class Strategy:
    def __init__(self):
        self.num_usages = 0
        self.choosing_time = 0
        self.applying_time = 0

    def invoke(self, sudoku_board):
        self.num_usages += 1
        timer = Timer()
        timer.startTimer()
        changes = self._findChanges(sudoku_board)
        self._applyChanges(sudoku_board, changes)
        self.applying_time += timer.stopTimer()

    def isAppropriate(self, sudoku_board):
        """Returns bool that indicates whether this strategy
           would work for a given sudoku board"""
        timer = Timer()
        timer.startTimer()
        if len(self._findChanges(sudoku_board)) == 0:
            self.choosing_time += timer.stopTimer()
            return False
        self.choosing_time += timer.stopTimer()
        return True

    def _findChanges(self, sudoku_board):
        return {}

    def _applyChanges(self, sudoku_board, changes):
        try:
            sudoku_board.setCell(changes['row'], changes['column'], changes['cell'])
        except KeyError:
            return
