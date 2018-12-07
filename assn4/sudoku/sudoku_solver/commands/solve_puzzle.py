from sudoku_solver.commands.command import Command


class SolvePuzzle(Command):
    def execute(self):
        self.receiver.solvePuzzle()
