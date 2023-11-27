from valuedGraph import ValuedGraph


def is_imposible_colored_graph(g: ValuedGraph, colors: list):
    for i in range(g.getNbVertice()):
        c = g.getVerticeValue(i + 1)
        if c != 0 and c not in colors:
            return False
        if c != 0:
            for v in g.getNeighbor(i + 1):
                if c == g.getVerticeValue(v):
                    return False
    return True


def get_lowest_free_color(g: ValuedGraph, i: int, colors: list):
    for i in g.getNeighbor(i):
        c = g.getVerticeValue(i)
        if c in colors:
            colors.remove(c)
    return colors[0]


def greedy_coloring(g: ValuedGraph, colors: list):
    assert len(colors) == g.getNbVertice() and all(
        [type(c) == int and c != 0 for c in colors]
    ), "greedy_coloring: colors list not valid."
    assert is_imposible_colored_graph(
        g, colors
    ), "greedy_coloring: the graph cannot be colored."

    for i in range(g.getNbVertice()):
        if g.getVerticeValue(i + 1) == 0:
            g.changeVerticeValue(i, get_lowest_free_color(g, i + 1, colors.copy()))


g = ValuedGraph(81)

for i in range(9):
    for j in range(9):
        for k in range(9):
            g.addEdge(i * 9 + j * 9 + )

print(g)

# g = ValuedGraph(9)

# for i in range(9):
#     for j in range(9):
#         if i != j:
#             g.addEdge(i + 1, j + 1)

# g.changeVerticeValue(1, 1)
# g.changeVerticeValue(3, 3)
# g.changeVerticeValue(4, 1)
# g.changeVerticeValue(9, 1)

# print(g)
# gp = greedy_coloring(g, [(n + 1) for n in range(9)])

# print(gp)
