import networkx as nx

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
        # Ensemble de tableau de sucesseurs
        self.g = {}
        # Ensemble des valeurs des sommets
        self.verticesValues = {}

    # Requetes

    def __str__(self) -> str:
        s = ""
        n = len(self.verticesValues)
        
        # Ajouter une ligne pour afficher les couleurs des sommets
        s += "Colors: " + ", ".join(str(self.verticesValues[i]) for i in range(1, n + 1)) + "\n"

        for i in range(1, n + 1):
            s += "| "
            for j in range(1, n + 1):
                # Ajouter la couleur du sommet (si elle existe) à la représentation
                color_i = self.verticesValues[i] if i in self.verticesValues else " "
                color_j = self.verticesValues[j] if j in self.verticesValues else " "
                
                s += f"{int(j in self.g[i])} ({color_i}/{color_j})"
                
                if j != n:
                    s += ", "
            s += " |"
            if i != n:
                s += "\n"
        return s
    
    def to_networkx_graph(self) -> nx.Graph:
        G = nx.Graph()
        for i in range(1, self.getNbVertice() + 1):
            G.add_node(i, color=self.getVerticeValue(i))

        for i in range(1, self.getNbVertice() + 1):
            neighbors = self.getNeighbor(i)
            for neighbor in neighbors:
                G.add_edge(i, neighbor)

        return G

    def getNbVertice(self) -> int:
        return len(self.verticesValues)

    def isAdjacent(self, i: int, j: int) -> bool:
        assert (
            i > 0
            and j > 0
            and i <= len(self.verticesValues)
            and j <= len(self.verticesValues)
        ), "isAdjacent : Out of bound"

        return j in self.g[i] or i == j

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
    
    def reset(self):
        self.g = {}
        self.verticesValues = {}

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