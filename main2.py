def lowest_int_not_in(list: list):
    sort_list = sorted(list)
    lowest = 1
    
    for n in sort_list:
        if n <= lowest:
            lowest = n + 1
    return lowest

class DynamicColoring:
    
    # CONSTRUCTEURS
    
    def __init__(self):

        self.g = {}
        self.verticesValues = {}

    # Requetes

    def __str__(self) -> str:
        s = ""
        n = len(self.verticesValues)
        for i in range(1, n + 1):
            s += "| "
            for j in range(1, n + 1):
                s += str(int(j in self.g[i]))
                if j != n:
                    s += ", "
            s += " |"
            if i != n:
                s += "\n"
        return s

    def getNbVertice(self) -> int:
        return len(self.verticesValues)

    def isAdjacent(self, i: int, j: int) -> bool:
        assert (
            i > 0
            and j > 0
            and i <= len(self.verticesValues)
            and j <= len(self.verticesValues)
        ), "isAdjacent : Out of bound"

        return j in self.g[i]

    def getNeighbor(self, i: int) -> list:
        assert i > 0 and i <= len(self.verticesValues), "getNeighbor : Out of bound"

        return self.g[i]

    def getVerticeValue(self, i: int) -> int:
        assert i > 0 and i <= len(self.verticesValues), "getVerticeValue : Out of bound"

        return self.verticesValues[i]
    
    def getValence(self, i:int) -> int:
        assert i > 0 and i <= len(self.verticesValues), "getValence : Out of bound"

        return len(self.g[i])
    
    def getValences(self) -> list:
        return [self.getValence(i + 1) for i in range(len(self.verticesValues))]

    # Commandes

    def addVertice(self):
        self.g[len(self.verticesValues) + 1] = []
        self.verticesValues[len(self.verticesValues) + 1] = 1

    def addEdge(self, i: int, j: int):
        assert (
            i > 0
            and j > 0
            and i <= len(self.verticesValues)
            and j <= len(self.verticesValues)
        ), "AddEdge : Out of bound"

        if j in self.g[i]:
            return
        self.g[j].append(i)
        self.g[i].append(j)
        if self.verticesValues[j] != self.verticesValues[i]:
            return
        if len(self.g[i]) > len(self.g[j]):
            l = list(map(lambda x: self.verticesValues[x], self.g[j]))
            l.append(self.verticesValues[i])
            self.verticesValues[j] = lowest_int_not_in(l)
            return
        l = list(map(lambda x: self.verticesValues[x], self.g[i]))
        l.append(self.verticesValues[j])
        self.verticesValues[i] = lowest_int_not_in(l)

def main():
    d = DynamicColoring()
    print(d)
    d.addVertice()
    d.addVertice()
    print(d)
    print(d.verticesValues)

    d.addEdge(1, 2)
    print(d)
    print(d.verticesValues)


if __name__ == "__main__":
    main()