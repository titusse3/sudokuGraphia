import numpy as np

# Le python c'est nul

class Graph(object):

    # Constructeur
    
    def __init__(self, n : int):
        assert n > 0, "Error: Bad arguments"

        self.matrice = np.zeros((n, n), dtype=int)
        self.n = n

    # Requetes

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

    def isAdjacent(self, i: int, j: int) -> bool :
        """Renvois vrais si les sommets de numéro i et j, sont adjacents. 
                faux sinon

        Args:
            i (int): Numéro de sommet
            j (int): Numéro de sommet

        Returns:
            bool: vrais si les sommets de numéro i et j, sont adjacents. faux 
                sinon
        """        
        assert i > 0 and j > 0 and i <= self.n and j <= self.n, "Error : Bad argument"
        
        return self.matrice[i - 1, j - 1] != 0

    def getNbVertices(self) -> int :
        """Renvois le nombre de sommet du graphe

        Returns:
            int: Nombre de sommet du graphe
        """        
        return self.n

    def getNeighbors(self, i: int) -> list:
        """Renvois la liste des successeurs du sommet de numéro i

        Args:
            i (int): Numéro de sommet

        Returns:
            list: Liste des successeurs du sommet de numéro i
        """            
        assert i > 0 and i <= self.n, "Error : Bad argument"
        
        return [n + 1 for n in range(0, self.matrice) if n != 0]
    
    # Commandes
    
    def addEdge(self, i: int, j: int) -> None:
        """Ajoute une arrête entre le sommet de numéro i et le sommet de numéro 
            j

        Args:
            i (int): Numéro de sommet
            j (int): Numéro de sommet
        """        
        assert i > 0 and j > 0 and i <= self.n and j <= self.n, "Error : Bad argument"

        self.matrice[i - 1, j - 1] = 1

class ValuedGraph(Graph):
    # Requete

    def getValue(self, i: int, j: int) -> int:
        """Renvoie la valeur sur l'arrête entre le sommet i et j

        Args:
            i (int): Numéro de sommet
            j (int): Numéro de sommet

        Returns:
            int: Valeur sur l'arrête entre le sommet i et j
        """        
        assert i > 0 and j > 0 and i <= self.n and j <= self.n, "Error : Bad argument"
        
        return self.matrice[i - 1, j - 1]

    # Commande

    def setValue(self, i: int, j: int, v: int) -> int:
        """Change la valeur sur l'arrête entre le sommet i et j

        Args:
            i (int): Numéro de sommet
            j (int): Numéro de sommet
            v (int): Nouvelle valeur de l'arrête

        Returns:
            int: Renvoie l'ancienne valeur sur l'arrête
        """        
        assert i > 0 and j > 0 and i <= self.n and j <= self.n, "Error : Bad argument"

        p = self.matrice[i - 1, j - 1]
        self.matrice[i - 1, j - 1] = v
        return p