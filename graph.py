import numpy as np


class Graph:
    def __init__(self, s=0):
        self.matrice = np.zeros((s, s), dtype=int)
        self.n = s

    def __str__(self) -> str:
        s = ""
        for i in range(self.n):
            s += "| "
            for j in range(self.n):
                s += str(self.matrice[i, j])
                if j != self.n - 1:
                    s += " "
            s += " |"
            if i != self.n - 1:
                s += "\n"
        return s


print(Graph(3))
