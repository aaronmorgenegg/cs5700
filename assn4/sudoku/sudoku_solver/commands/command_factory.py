from sudoku_solver.commands.solve_cell import SolveCell
from sudoku_solver.commands.solve_puzzle import SolvePuzzle
from sudoku_solver.commands.undo import Undo

COMMANDS = {"solve_cell": SolveCell,
            "solve_puzzle": SolvePuzzle,
            "undo": Undo}

class CommandFactory:
    @staticmethod
    def build(command_name, receiver):
        return COMMANDS[command_name](receiver)
