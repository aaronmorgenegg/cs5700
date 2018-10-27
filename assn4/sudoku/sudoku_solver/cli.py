import argparse
import os


class CLI:
    def __init__(self):
        self.parser = self._initParser()
        self.args = vars(self.parser.parse_args())
        self._processArgs()

    def _initParser(self):
        parser = argparse.ArgumentParser(description='Sudoku Solver')
        parser.add_argument('-i', '--input', help='Input puzzle file or directory', required=True)
        parser.add_argument('-o', '--output', help='Output puzzle file or directory')
        return parser

    def _processArgs(self):
        directory_mode = False
        if os.path.isfile(self.args['input']):
            input_root = "Input"
            input_file = self.args['input']
        else:
            input_root = self.args['input']
            directory_mode = True

        if self.args['output']:
            if os.path.isfile(self.args['output']):
                output_root = "Output"
                output_file = self.args['output']
            else:
                output_root = self.args['output']
                directory_mode = True

        if directory_mode:
            pass
        else:
            self._solveFile(input_file, output_root + "/" + output_file)

    def _solveFile(self, input_file, output_file):
        pass

    def _solveDirectory(self, input_dir, output_dir):
        pass
