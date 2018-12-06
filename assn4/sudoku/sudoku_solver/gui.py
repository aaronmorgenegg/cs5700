from tkinter import *
from tkinter import messagebox, filedialog

from sudoku_solver.puzzle_reader import PuzzleReader
from sudoku_solver.sudoku_board import SudokuBoard
from sudoku_solver.sudoku_solver import SudokuSolver


class GUI:
    def __init__(self):
        self.puzzle_reader = PuzzleReader()
        self._initOptions()
        self._initWindow()
        self._initMenu()
        self._initButtons()
        self._initBoard()
        self._startGUI()

    def _initOptions(self):
        self.btn_position=0
        self.showPossibilities = False

    def _initWindow(self):
        self.window = Tk()
        self.window.geometry("750x800")
        self.window.title("Sudoku Solver")

    def _initButtons(self):
        self._addButton("Solve Square", self._solveSquare)
        self._addButton("Solve Puzzle", self._solvePuzzle)
        self._addButton("Undo", self._undo)

    def _addButton(self, name, function):
        btn = Button(self.window, text=name, command=function)
        btn.grid(column=self.btn_position, row=26)
        self.btn_position += 1

    def _initMenu(self):
        menu = Menu(self.window)
        sub_menu = Menu(menu, tearoff=0)

        sub_menu.add_command(label='Load', command=self._loadPuzzle)
        sub_menu.add_command(label='Save', command=self._savePuzzle)
        sub_menu.add_command(label='Toggle Possibilities', command=self._togglePossibilities)
        menu.add_cascade(label='Menu', menu=sub_menu)
        self.window.config(menu=menu)

    def _startGUI(self):
        self.window.mainloop()

    def _initBoard(self):
        pass

    def _loadPuzzle(self):
        filename = filedialog.askopenfilename()

        board = self.puzzle_reader.loadPuzzle(filename)
        if type(board) == SudokuBoard:
            self.sudoku_solver = SudokuSolver(board)
        elif type(board) == str:
            self._displayMessage(board, "Parse Error")

    def _savePuzzle(self):
        filename = filedialog.askopenfilename()
        self.puzzle_reader.savePuzzle(self.sudoku_solver.toString(), filename)
        self._displayMessage("Saved puzzle to {}".format(filename), "Success")

    def _solveSquare(self):
        pass

    def _solvePuzzle(self):
        pass

    def _togglePossibilities(self):
        self.showPossibilities = not self.showPossibilities

    def _undo(self):
        pass

    def _displayMessage(self, message, title='Message'):
        messagebox.showinfo(title, message)
