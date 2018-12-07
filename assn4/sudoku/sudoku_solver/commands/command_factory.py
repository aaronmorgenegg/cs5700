from sudoku_solver.commands.solve_cell import SolveCell

COMMANDS = {"solve_cell": SolveCell}

class CommandFactory:
    @staticmethod
    def build(command_name, receiver):
        return COMMANDS[command_name](receiver)
