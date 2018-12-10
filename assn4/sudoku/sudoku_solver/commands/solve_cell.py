from sudoku_solver.commands.command import Command


class SolveCell(Command):
    def invoke(self):
        self.receiver.tryStrategy()
