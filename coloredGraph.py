from graph import Graph, ValuedGraph

def get_smallest_value()

def greed_coloring(g: ValuedGraph) -> (int, ValuedGraph):
    vertices = [n for n in range(1, g.getNbVertices() + 1)]
    colored_graph = ValuedGraph(g.getNbVertices())
    current = 0
    for n in vertices:
        k = get_smallest_value(colored_graph, n, g.getNeighbors(n))

        if 
    return colored_graph


def backTracking(g: ValuedGraph) -> ValuedGraph:
    return g