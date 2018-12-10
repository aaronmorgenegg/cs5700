from sudoku_solver.commands.command import Command


class Undo(Command):
    def invoke(self):
        self.receiver.undo()
