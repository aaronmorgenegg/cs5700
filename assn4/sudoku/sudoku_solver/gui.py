from tkinter import *
from tkinter import messagebox, filedialog

from sudoku_solver.commands.command_factory import CommandFactory
from sudoku_solver.constants import BLANK_CELL
from sudoku_solver.puzzle_reader import PuzzleReader
from sudoku_solver.sudoku_board import SudokuBoard
from sudoku_solver.sudoku_solver import SudokuSolver


CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
CELL_FONT_SIZE = {4: 40, 9: 25, 16:16, 25:9}

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
        self.btn_position = 0
        self.showPossibilities = False
        self.sudoku_solver = None

    def _initWindow(self):
        self.window = Tk()
        self.window.geometry("600x700")
        self.window.title("Sudoku Solver")

    def _initButtons(self):
        self._addButton("Solve Cell", self._solveCell)
        self._addButton("Solve Puzzle", self._solvePuzzle)
        self._addButton("Undo", self._undo)

    def _addButton(self, name, function):
        btn = Button(self.window, text=name, command=function)
        btn.grid(column=0, row=self.btn_position)
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
        self.canvas = Canvas(self.window, height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
        self.canvas.grid(column=0, row=self.btn_position)
        self._drawBoard()

    def _drawBoard(self):
        self.canvas.delete("all")

        x = 7
        y = 2
        if self.sudoku_solver is None:
            board_size = 9
        else:
            board_size = len(self.sudoku_solver.sudoku_board.rows)
        cell_size = CANVAS_WIDTH/board_size-2
        for i in range(board_size):
            for j in range(board_size):
                self.canvas.create_rectangle(x, y, x+cell_size, y+cell_size)
                if self.sudoku_solver is None:
                    cell = BLANK_CELL
                else:
                    cell = self.sudoku_solver.sudoku_board.rows[i][j]
                if cell != BLANK_CELL:
                    self.canvas.create_text(x+cell_size/2, y+cell_size/2, text=cell,
                                            font="Times {} bold".format(CELL_FONT_SIZE[board_size]))
                x += cell_size
            y += cell_size
            x = 7

    def _loadPuzzle(self):
        filename = filedialog.askopenfilename()

        board = self.puzzle_reader.loadPuzzle(filename)
        if type(board) == SudokuBoard:
            self.sudoku_solver = SudokuSolver(board)
        elif type(board) == str:
            self._displayMessage(board, "Parse Error")
        self._drawBoard()

    def _savePuzzle(self):
        filename = filedialog.askopenfilename()
        self.puzzle_reader.savePuzzle(self.sudoku_solver.toString(), filename)
        self._displayMessage("Saved puzzle to {}".format(filename), "Success")

    def _solveCell(self):
        self._executeCommand("solve_cell")

    def _solvePuzzle(self):
        self._executeCommand("solve_puzzle")

    def _togglePossibilities(self):
        self.showPossibilities = not self.showPossibilities

    def _undo(self):
        self._executeCommand("undo")

    def _executeCommand(self, command_name):
        command = CommandFactory.build(command_name, self.sudoku_solver)
        command.execute()
        self._drawBoard()

    def _displayMessage(self, message, title='Message'):
        messagebox.showinfo(title, message)
