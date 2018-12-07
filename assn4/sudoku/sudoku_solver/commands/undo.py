from sudoku_solver.commands.command import Command


class Undo(Command):
    def execute(self):
        self.receiver.undo()
