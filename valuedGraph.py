import numpy as np


class ValuedGraph:
    def __init__(self, n: int):
        assert n > 0, "__init__ : them matrice must have positive a size."

        self.matrice = np.zeros((n, n), dtype=int)
        self.verticesValues = np.zeros(n, dtype=int)

    # Requetes

    def __str__(self):
        s = ""
        n = len(self.verticesValues)
        for i in range(n):
            s += "| "
            for j in range(n):
                s += str(self.matrice[i, j])
                if j != n - 1:
                    s += ", "
            s += " |"
            if i != n - 1:
                s += "\n"
        return s

    def getNbVertice(self):
        return len(self.verticesValues)

    def isAdjacent(self, i: int, j: int):
        assert (
            i > 0
            and j > 0
            and i <= len(self.verticesValues)
            and j <= len(self.verticesValues)
        ), "isAdjacent : Out of bound"

        return self.matrice[i - 1, j - 1] != 0

    def getNeighbor(self, i: int):
        assert i > 0 and i <= len(self.verticesValues), "getNeighbor : Out of bound"

        return [
            (n + 1)
            for n in range(len(self.verticesValues))
            if self.matrice[i - 1, n] != 0
        ]

    def getVerticeValue(self, i: int):
        assert i > 0 and i <= len(self.verticesValues), "getVerticeValue : Out of bound"

        return self.verticesValues[i - 1]

    # Commandes

    def addEdge(self, i: int, j: int):
        assert (
            i > 0
            and j > 0
            and i <= len(self.verticesValues)
            and j <= len(self.verticesValues)
        ), "AddEdge : Out of bound"

        self.matrice[i - 1, j - 1] = 1
        self.matrice[j - 1, i - 1] = 1

    def changeVerticeValue(self, i: int, v: int):
        assert i > 0 and i <= len(self.verticesValues), "getNeighbor : Out of bound"

        self.verticesValues[i - 1] = v
