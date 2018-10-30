import argparse
import os

from sudoku_solver.puzzle_reader import PuzzleReader
from sudoku_solver.sudoku_solver import SudokuSolver


class CLI:
    def __init__(self):
        self.parser = self._initParser()
        self.args = vars(self.parser.parse_args())

    def _initParser(self):
        parser = argparse.ArgumentParser(description='Sudoku Solver')
        parser.add_argument('-i', '--input', help='Input puzzle file or directory', required=True)
        parser.add_argument('-o', '--output', help='Output puzzle file or directory')
        return parser

    def processArgs(self):
        output_dir, output_file = self._processOutput()

        if os.path.isfile(self.args['input']):
            input_file = self.args['input']
            self._solveFile(input_file, output_dir + "/" + output_file)
        else:
            input_dir = self.args['input']
            self._solveDirectory(input_dir, output_dir)

    def _processOutput(self):
        output_dir = "sample_puzzles/output"
        output_file = self.args['input'].split("/").pop()
        if self.args['output']:
            if os.path.isfile(self.args['output']):
                output_file = self.args['output']
            else:
                output_dir = self.args['output']
        return output_dir, output_file

    def _solveFile(self, input_file, output_file):
        puzzle_reader = PuzzleReader()
        board = puzzle_reader.loadPuzzle(input_file)
        sudoku_solver = SudokuSolver(board)
        puzzle_reader.savePuzzle(sudoku_solver.solvePuzzle(), output_file)

    def _solveDirectory(self, input_dir, output_dir):
        for filename in os.listdir(input_dir):
            self._solveFile(input_dir+"/"+filename, output_dir+"/"+filename)
