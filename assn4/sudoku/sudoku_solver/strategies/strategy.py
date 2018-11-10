from sudoku_solver.timer import Timer


class Strategy:
    def __init__(self):
        self.num_usages = 0
        self.choosing_time = 0
        self.applying_time = 0

    def invoke(self, sudoku_board):
        timer = Timer()
        timer.startTimer()
        coords = self._findCoords(sudoku_board)
        self._applyChanges(sudoku_board, coords)
        self.applying_time += timer.stopTimer()

    def isAppropriate(self, sudoku_board):
        """Returns bool that indicates whether this strategy
           would work for a given sudoku board"""
        timer = Timer()
        timer.startTimer()
        if len(self._findCoords(sudoku_board)) == 0:
            self.choosing_time += timer.stopTimer()
            return False
        self.choosing_time += timer.stopTimer()
        return True

    def _findCoords(self, sudoku_board):
        return {}

    def _applyChanges(self, sudoku_board, coords):
        pass
