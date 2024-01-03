from valuedGraph import ValuedGraph
from math import sqrt
import sudoku
from coloredGraph import greedy_coloring, welsh_powell_coloring, backtracking_coloring
from enum import Enum
from pprint import pprint

# https://www.kleemans.ch/static/fourcolors/welsh-powell.pdf
# https://people.cs.uchicago.edu/~laci/14algorithms/greedycoloring.pdf
# https://github.com/jeffsieu/py-sudoku

def coord_to_index(i: int, j: int, n: int) -> int:
    return i * n + j + 1

def sudoku_to_graph(sudoku: list) -> ValuedGraph:

    n = len(sudoku)
    g = ValuedGraph(n * n)
    
    for i in range(n):
        for j in range(n):
            value = sudoku[i][j]
            if value != 0:
                g.changeVerticeValue(coord_to_index(i, j, n), value)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if k != j:
                    g.addEdge(coord_to_index(i, j, n), coord_to_index(i, k, n))
                if k != i:
                    g.addEdge(coord_to_index(i, j, n), coord_to_index(k, j, n))

            sqrt_n = int(sqrt(n))

            block_i = sqrt_n * (i // sqrt_n)
            block_j = sqrt_n * (j // sqrt_n)
            for x in range(block_i, block_i + sqrt_n):
                for y in range(block_j, block_j + sqrt_n): 
                    if x != i and y != j:
                        g.addEdge(coord_to_index(i, j, n), coord_to_index(x, y, n))

    return g

class Algo(Enum):
    POWELL = 1
    GREEDY = 2
    BACKTRACKING = 3

    def __str__(self) -> str:
        return "Truc de malade"


class Sudoku:
    def __init__(self):
        self.size = 3
        self.g = None
        self.colors = [(n + 1) for n in range(self.size ** 2)]

    def getSudoku(self) -> list:
        assert self.g != None, "getSudoku: Generate the sudoku before."
        sudoku = []
        for i in range(self.size ** 2):
            sub = []
            for j in range(self.size ** 2):
                sub.append(self.g.getVerticeValue(coord_to_index(i, j, self.size)))
            sudoku.append(sub)
        return sudoku 
    
    def verify(self) -> bool:
        for i in range(1, self.g.getNbVertice() + 1):
            c = self.g.getVerticeValue(i)
            if c != 0 and c not in self.colors:
                return False
            if c != 0:
                for v in self.g.getNeighbor(i):
                    if c == self.g.getVerticeValue(v):
                        return False
        return True
    
    def resetSudoku(self) -> None:
        self.g = None

    def getColors(self) -> list:
        return self.colors.copy()

    def generate(self, difficulty: float) -> None:
        puzzle = sudoku.Sudoku(self.size).difficulty(difficulty)
        self.g = sudoku_to_graph([[0 if element is None else element for element in sous_liste] for sous_liste in puzzle.board])

    def solve(self, algo: Algo) -> bool:
        assert self.g != None, "solve: Generate the sudoku before solving."
        match algo:
            case Algo.POWELL:
                return welsh_powell_coloring(self.g, self.colors)
            case Algo.GREEDY:
                return greedy_coloring(self.g, self.colors)
            case Algo.BACKTRACKING:
                return backtracking_coloring(self.g, self.colors)
            
    def setValue(self, case: int, value: int) -> None:
        assert case > 0 and case < self.size ** 4, "setValue: Outbound index."
        assert value in self.colors, "setValue: Invalide value."

        self.g.changeVerticeValue(case, value)

if __name__ == "__main__":
    s = Sudoku()
    s.generate(0.5)
    pprint(s.getSudoku())
    print(s.solve(Algo.BACKTRACKING))
    pprint(s.getSudoku())
    s.resetSudoku()
    s.generate(0.5)
    s.setValue(5, 5)
    print(s.verify())
    print(Algo.BACKTRACKING)