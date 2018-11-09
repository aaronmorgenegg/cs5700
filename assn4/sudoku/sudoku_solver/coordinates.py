import math

from sudoku_solver.constants import COLUMN_MODE, BLOCK_MODE


class Coordinates:
    @staticmethod
    def convert(x, y, mode, size):
        """Converts coordinates from columns or blocks into row coordinates"""
        if mode.lower() in COLUMN_MODE:
            return y, x
        elif mode.lower() in BLOCK_MODE:
            block_size = int(math.sqrt(size))
            block = (x//block_size)*block_size+(y//block_size)
            index = (x%block_size)*block_size+(y%block_size)
            return block, index
        else:
            return x, y
