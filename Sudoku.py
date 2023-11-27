import numpy as np

class Sudoku:
    def __init__(self, n: int):
        assert n > 0, "Error: Bad argument"

        self.grid = np.zeros((n, n), dtype=int)