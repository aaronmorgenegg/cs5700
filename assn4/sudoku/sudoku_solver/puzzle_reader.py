from sudoku_solver.sudoku_board import SudokuBoard
from sudoku_solver.sudoku_board_exception import SudokuBoardException


class PuzzleReader:
    def loadPuzzle(self, filename):
        try:
            data = self._readFileToList(filename)
            size = int(data.pop(0))
            valid_symbols = data.pop(0).strip().split(" ")
            board = [x.strip().split(" ") for x in data if len(x) >= 2]
            return SudokuBoard(size, valid_symbols, board)
        except SudokuBoardException:
            data = self._readFileToList(filename)
            return ''.join(data) + "\nBad Puzzle"

    def savePuzzle(self, puzzle_string, filename):
        with open(filename, 'w') as f:
            f.write(puzzle_string)

    def _readFileToList(self, filename):
        with open(filename, 'r') as f:
            content = f.readlines()
        return content
