

class SudokuBoard:
    def __init__(self, size, valid_symbols, initial_board):
        self.size = size
        self.valid_symbols = valid_symbols
        self.initial_board = initial_board
        self.current_board = initial_board

    def toString(self):
        string = ""
        string += str(self.size) + "\n"
        for symbol in self.valid_symbols:
            string += str(symbol) + " "
        string += "\n"
        string += self._boardToString(self.initial_board)
        string += "Solution:\n"
        string += self._boardToString(self.current_board)
        return string

    def _boardToString(self, board):
        string = ""
        for row in board:
            for cell in row:
                string += cell + " "
            string += "\n"
        return string
