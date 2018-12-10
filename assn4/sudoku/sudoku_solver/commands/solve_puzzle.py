from sudoku_solver.commands.command import Command


class SolvePuzzle(Command):
    def invoke(self):
        self.receiver.solvePuzzle()
