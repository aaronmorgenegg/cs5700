from sudoku_solver.commands.command import Command


class SolveCell(Command):
    def execute(self):
        self.receiver.tryStrategy()
