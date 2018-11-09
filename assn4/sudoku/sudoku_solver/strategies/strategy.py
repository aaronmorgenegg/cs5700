

class Strategy:
    def invoke(self, sudoku_board):
        coords = self._findCoords(sudoku_board)
        self._applyChanges(sudoku_board, coords)

    def isAppropriate(self, sudoku_board):
        """Returns bool that indicates whether this strategy
           would work for a given sudoku board"""
        if len(self._findCoords(sudoku_board)) == 0:
            return False
        return True

    def _findCoords(self, sudoku_board):
        return {}

    def _applyChanges(self, sudoku_board, coords):
        pass
