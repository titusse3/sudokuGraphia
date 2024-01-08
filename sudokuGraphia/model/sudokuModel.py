from math import sqrt
from .valuedGraph import ValuedGraph
from .sudokuGen import Sudoku
from .coloredGraph import greedy_coloring, welsh_powell_coloring, backtracking_coloring
from enum import Enum
from pprint import pprint
import time

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
    NO_ALGO = 0
    POWELL = 1
    GREEDY = 2
    BACKTRACKING = 3

    def __str__(self):
        match self:
            case Algo.NO_ALGO:
                return ("Cette fonctionnalité vous permet de jouer au Sudoku.\n"
                + "Un  fois vos réponses entrée, appuyez sur le boutton "
                + "'Vérifier' pour savoir si vos réponses sont correctes.\n" +
                "Bon jeu ! 😁\n\n\n\n\n\n\n𝓪𝓶𝓸𝓰𝓾𝓼 ඞ\n  🦋⃤♡⃤🌈⃤")
            case Algo.POWELL:
                return ("L'algorithme de coloration de graphes de Powell est un" 
                    + " algorithme classique utilisé pour attribuer des couleurs"
                    + " aux sommets d'un graphe de manière à ce que deux sommets"
                    + " adjacents n'aient jamais la même couleur. L'objectif est"
                    + " de minimiser le nombre total de couleurs utilisées.\n\n"
                    + "L'algorithme de coloration de graphes de Powell suit ces"
                    + " étapes de base :\n\n"
                    + "Tri des sommets : Triez les sommets du graphe par degré"
                    + " décroissant, ce qui signifie que les sommets avec un "
                    + "plus grand nombre de voisins sont traités en premier.\n\n"
                    + "Initialisation : Associez la première couleur au premier"
                    + " sommet de la liste triée. Puis, pour chaque sommet "
                    + "suivant, attribuez la plus petite couleur possible qui "
                    + "n'a pas encore été utilisée par ses voisins.\n"
                    + "Réarrangement des couleurs : Réarrangez la liste des "
                    + "couleurs de manière à ce que les couleurs utilisées par "
                    + "un sommet apparaissent dans l'ordre croissant.\n\n"
                    + "Répétition : Répétez les étapes 2 et 3 jusqu'à ce que "
                    + "tous les sommets soient colorés.\n"
                    + "L'avantage de l'algorithme de coloration de graphes de "
                    + "Powell réside dans son efficacité pour de nombreux types "
                    + "de graphes, en particulier ceux avec une structure "
                    + "régulière. Cependant, il peut ne pas être aussi efficace "
                    + "sur des graphes irréguliers ou complexes.\n\n"
                    + "En résumé, l'algorithme de coloration de graphes de "
                    + "Powell offre une approche heuristique pour résoudre le "
                    + "problème de coloration de graphes, en exploitant la" 
                    + "structure du graphe pour minimiser le nombre de couleurs "
                    + "nécessaires.")          
            case Algo.GREEDY:
                return (
                    "🍔 L'algorithme glouton de coloration de graphe, également appelé "
                    + "algorithme de coloration séquentielle, est une méthode simple et "
                    + "efficace pour attribuer des couleurs aux sommets d'un graphe. Voici une "
                    + "description concise de l'algorithme :\n\n"
                    + "    Tri des sommets : Triez les sommets du graphe par degré décroissant, "
                    + "de sorte que les sommets ayant le plus grand nombre de voisins soient "
                    + "traités en premier.\n\n"
                    + "    Coloration séquentielle : Pour chaque sommet dans l'ordre trié, "
                    + "attribuez-lui la plus petite couleur possible qui n'a pas encore été "
                    + "utilisée par ses voisins.\n\n"
                    + "    Répétition : Répétez l'étape 2 jusqu'à ce que tous les sommets "
                    + "soient colorés.\n\n"
                    + "L'algorithme glouton de coloration de graphe vise à minimiser le nombre "
                    + "total de couleurs utilisées tout en garantissant que deux sommets "
                    + "adjacents n'ont pas la même couleur. Cependant, il ne garantit pas une "
                    + "coloration optimale, et le nombre de couleurs utilisées peut être "
                    + "sensiblement plus élevé que la chromaticité minimale du graphe (nombre "
                    + "minimum de couleurs nécessaires).\n\n"
                    + "Cet algorithme est simple et rapide, ce qui le rend pratique pour les "
                    + "graphes de taille modérée. Cependant, il peut ne pas fournir la meilleure "
                    + "solution dans tous les cas, car il peut conduire à des colorations "
                    + "sous-optimales dans certains graphes complexes. 🥐")   
            case Algo.BACKTRACKING:
                return (
                    "👨‍💻 L'algorithme de coloration de graphes en utilisant la méthode du "
                    + "backtracking est une approche récursive qui cherche à attribuer des "
                    + "couleurs aux sommets d'un graphe de manière à ce que deux sommets "
                    + "adjacents n'aient jamais la même couleur. Voici une description concise "
                    + "de l'algorithme :\n\n"
                    + "1. Choix d'une couleur : Commencez par attribuer une couleur au premier "
                    + "sommet du graphe.\n\n"
                    + "2. Validation : Pour chaque sommet suivant, essayez de lui attribuer une "
                    + "couleur en vérifiant qu'aucun de ses voisins n'a la même couleur. Si une "
                    + "couleur est valide, passez au sommet suivant ; sinon, revenez en arrière "
                    + "(backtrack)🔙 et explorez d'autres choix.\n\n"
                    + "3. Terminaison : Répétez le processus jusqu'à ce que tous les sommets "
                    + "soient colorés ou que toutes les possibilités aient été explorées.\n\n"
                    + "4. Retour en arrière : Si une configuration ne mène pas à une solution "
                    + "valide, revenez en arrière (backtrack) pour explorer d'autres options.\n\n"
                    + "L'algorithme utilise la récursion pour explorer toutes les combinaisons "
                    + "possibles de couleurs tout en évitant les configurations invalides. Bien "
                    + "que la méthode de backtracking puisse être coûteuse en termes de temps "
                    + "d'exécution dans certains cas, elle garantit une solution correcte si "
                    + "elle existe."
                )


class SudokuModel:
    
    # Constructeur
    
    def __init__(self):
        self.size = 3
        self.g = None
        self.colors = [(n + 1) for n in range(self.size ** 2)]
        self.algoType = Algo.NO_ALGO
        
    # Requetes
    
    def getSudokuLength(self) -> int:
        return self.size ** 2
    
    def isGenerated(self) -> bool:
        return self.g != None
    
    def getAlgo(self) -> Algo:
        return self.algoType
    
    def getColors(self) -> list:
        return self.colors.copy()

    def getSudoku(self) -> list:
        assert self.g != None, "getSudoku: Generate the sudoku before."
        sudoku = []
        for i in range(self.size ** 2):
            sub = []
            for j in range(self.size ** 2):
                sub.append(self.g.getVerticeValue(coord_to_index(i, j, self.size ** 2)))
            sudoku.append(sub)
        return sudoku 
    
    def isPossible(self) -> bool:
        for i in range(1, self.g.getNbVertice() + 1):
            c = self.g.getVerticeValue(i)
            if c != 0 and c not in self.colors:
                return False
            if c != 0:
                for v in self.g.getNeighbor(i):
                    if c == self.g.getVerticeValue(v):
                        return False
        return True

    def isSolve(self) -> bool:
        for i in range(1, self.g.getNbVertice() + 1):
            if self.g.getVerticeValue(i) == 0:
                return False
        return self.isPossible()
    
    # Commandes
    
    def resetSudoku(self) -> None:
        self.g = None

    def generate(self, difficulty: float) -> None:
        puzzle = Sudoku(self.size, seed=time.time()).difficulty(difficulty)
        self.g = sudoku_to_graph([[0 if element is None else element for element in sous_liste] for sous_liste in puzzle.board])
        
    def setAlgo(self, algo: Algo) -> None:
        self.algoType = algo

    def solve(self) -> bool:
        assert self.g != None, "solve: Generate the sudoku before solving."
        match self.algoType:
            case Algo.POWELL:
                if not self.isPossible():
                    return False;
                return welsh_powell_coloring(self.g, self.colors)
            case Algo.GREEDY:
                if not self.isPossible():
                    return False;
                return greedy_coloring(self.g, self.colors)
            case Algo.BACKTRACKING:
                if not self.isPossible():
                    return False;
                return backtracking_coloring(self.g, self.colors)
            case Algo.NO_ALGO:
                return self.isPossible()      
            
    def setValue(self, case: int, value: int) -> None:
        assert case > 0 and case <= self.size ** 4, "setValue: Outbound index."
        assert value in self.colors or value == 0, "setValue: Invalide value."

        self.g.changeVerticeValue(case, value)

if __name__ == "__main__":
    s = SudokuModel()
    s.generate(0.5)
    pprint(s.getSudoku())
    s.setAlgo(Algo.BACKTRACKING)
    print(s.solve())
    pprint(s.getSudoku())
    s.resetSudoku()
    print("gen")
    s.generate(0.5)
    pprint(s.getSudoku())
    print(s.isSolved())
    s.setValue(81, 5)
    pprint(s.getSudoku())
    print(s.isSolved())