from sudoku_solver.timer import Timer


class Strategy:
    def __init__(self):
        self.num_usages = 0
        self.choosing_time = 0
        self.applying_time = 0
        self.type = None
        self.change = None

    def invoke(self, sudoku_board, choices):
        self.num_usages += 1
        timer = Timer()
        timer.startTimer()
        changes = self._findChanges(sudoku_board, choices)
        if self.type == "solve":
            self._applyChanges(sudoku_board, changes)
        elif self.type == "choice":
            self._applyChanges(choices, changes)
        self.applying_time += timer.stopTimer()
        return self.change

    def isAppropriate(self, sudoku_board, choices):
        """Returns bool that indicates whether this strategy
           would work for a given sudoku board"""
        timer = Timer()
        timer.startTimer()
        if len(self._findChanges(sudoku_board, choices)) == 0:
            self.choosing_time += timer.stopTimer()
            return False
        self.choosing_time += timer.stopTimer()
        return True

    @staticmethod
    def undo(sudoku_board, change):
        if change is not None:
            sudoku_board.setCell(change['row'], change['column'], change['old'])

    def _findChanges(self, sudoku_board, choices):
        return {}

    def _applyChanges(self, target, changes):
        try:
            if self.type == "choice":
                target[changes['row']][changes['column']] = changes['choice_list']
            elif self.type == "solve":
                self.change = {'type': self.__class__.__name__, 'row': changes['row'], 'column': changes['column'],
                               'old': target.getCell(changes['row'], changes['column']), 'new': changes['cell']}
                target.setCell(changes['row'], changes['column'], changes['cell'])
        except KeyError:
            return
