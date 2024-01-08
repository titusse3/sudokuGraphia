from .valuedGraph import ValuedGraph

def get_lowest_free_color(g: ValuedGraph, color: set, i: int, colors: list):
    colors_ = colors.copy()
    for i in g.getNeighbor(i):
        c = color[i]
        if c in colors_:
            colors_.remove(c)
    if len(colors_) == 0:
        return None
    return colors_[0]

def greedy_coloring(g: ValuedGraph, colors: list) -> bool:
    n = g.getNbVertice()
    color = {}
    for i in range(1, n + 1):
        color[i] = g.getVerticeValue(i)

    for i in range(n):
        if color[i + 1] == 0:
            c = get_lowest_free_color(g, color, i + 1, colors)
            if c == None:
                return False
            color[i + 1] = c

    for i in range(1, n + 1):
        g.changeVerticeValue(i, color[i])
    return True

def welsh_powell_coloring(g: ValuedGraph, colors: list):
    n = g.getNbVertice()
    color = {}
    for i in range(1, n + 1):
        color[i] = g.getVerticeValue(i)

    valence_list = g.getValences()
    uncolored_vertice = [(i + 1, valence_list[i]) for i in range(g.getNbVertice()) if color[i + 1] == 0]
    sorted(uncolored_vertice, key=lambda x: x[1], reverse=True)

    for (n, _) in uncolored_vertice:
        c = get_lowest_free_color(g, color, n, colors)
        if c == None:
            return False
        color[n] = c
    
    for i in range(1, n + 1):
        g.changeVerticeValue(i, color[i])
    return True
    
def backtracking_coloring(g: ValuedGraph, colors: list) -> bool:
    n = g.getNbVertice()
    result = {}
    color = {}
    sum_result = 0

    # Initialisation du tableau color pour qu'il ait les sommets déjà coloré
    for i in range(1, n + 1):
        color[i] = g.getVerticeValue(i)

    sum_color = sum(color.values())

    def is_safe(vertex: int, c: int) -> bool:
        '''
        Fonction qui vérifie si la couleur color est possible pour le sommet vertex
        '''
        used_colors = set(color[neighbor] for neighbor in g.getNeighbor(vertex) if color[neighbor] != 0)
        return c not in used_colors
    
    def backtracking_coloring_aux(vertex: int):
        '''
        Fonction qui va calculer la coloration optimal du graphe à partir du sommet vertex
        '''
        nonlocal color
        nonlocal result
        nonlocal sum_color
        nonlocal sum_result

        if sum_result != 0 and sum_color >= sum_result:
            return
        
        if vertex == n + 1:
            if sum_result == 0 or sum_color < sum_result:
                result = color.copy()
                sum_result = sum_color
            return
        
        if color[vertex] != 0:
            backtracking_coloring_aux(vertex + 1)
            return
        
        for c in range(1, len(colors) + 1):
            if is_safe(vertex, c):
                color[vertex] = c
                sum_color += c
                backtracking_coloring_aux(vertex + 1)
                sum_color -= c
                color[vertex] = 0

    backtracking_coloring_aux(1)

    if len(result) == 0:
        return False
    
    # Application de la coloration optimal sur le graphe
    for i in range(1, n + 1):
        g.changeVerticeValue(i, result[i])

    return True