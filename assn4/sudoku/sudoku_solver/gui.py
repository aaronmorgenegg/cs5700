from tkinter import *


class GUI:
    def __init__(self):
        self._initOptions()
        self._initWindow()
        self._initButtons()
        self._initBoard()
        self._startGUI()

    def _initOptions(self):
        self.btn_position=0

    def _initWindow(self):
        self.window = Tk()
        self.window.title("Sudoku Solver")

    def _initButtons(self):
        self._addButton("Load Puzzle", self._loadPuzzle)
        self._addButton("Save Puzzle", self._savePuzzle)
        self._addButton("Solve Square", self._solveSquare)
        self._addButton("Solve Puzzle", self._solvePuzzle)
        self._addButton("Toggle Possibilities", self._togglePossibilities)
        self._addButton("Undo", self._undo)

    def _addButton(self, name, function):
        btn = Button(self.window, text=name, command=function)
        btn.grid(column=0, row=self.btn_position)
        self.btn_position += 1

    def _startGUI(self):
        self.window.mainloop()

    def _initBoard(self):
        pass

    def _loadPuzzle(self):
        pass

    def _savePuzzle(self):
        pass

    def _solveSquare(self):
        pass

    def _solvePuzzle(self):
        pass

    def _togglePossibilities(self):
        pass

    def _undo(self):
        pass


myGui = GUI()
