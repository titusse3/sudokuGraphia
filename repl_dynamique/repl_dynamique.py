from DynamicColoring import DynamicColoring
import re
import matplotlib.pyplot as plt
import networkx as nx

def affiche_graphe(graph):
    g = graph.to_networkx_graph()

    # Dessinez le graphe
    pos = nx.spring_layout(g)  # Choisissez une disposition appropriée
    node_colors = [data["color"] for _, data in g.nodes(data=True)]

    nx.draw(g, pos, with_labels=True, node_size=700, node_color=node_colors, font_color="white", font_weight="bold")
    plt.show()

# Fonction pour exécuter le REPL
def run_calculator_repl():
    graph = DynamicColoring()
    commands = {
        'affiche': lambda : affiche_graphe(graph),
        'nombreSommet': graph.getNbVertice,
        'sontVoisin': graph.isAdjacent,
        'voisins': graph.getNeighbor,
        'obtenirCouleur': graph.getVerticeValue,
        'ajoutSommet': graph.addVertice,
        'ajoutArete': graph.addEdge,
        'reinitialiser': graph.reset
    }

    print("Bienvenue dans le REPL de construiction de graph colorer dynamique. " 
        "Tapez 'exit' pour quitter.")

    while True:
        user_input = input('>>> ')
        if user_input.lower() == 'exit':
            break
        
        if user_input.lower() == 'help':
            print("Les commandes disponibles sont :")
            print("\n".join(commands.keys()))
            continue

        try:
            command, *args = user_input.split()
            if command in commands:
                if args:
                    args = [int(arg)  for arg in args if re.sub(r'[^a-zA-Z0-9]', '', arg) != ''] 
                    commands[command](*args)
                else:
                    result = commands[command]()
                    if result != None:
                        print(result)
            else:
                print("Commande non reconnue.")
        except Exception as e:
            print(f"Error : {e}")

if __name__ == "__main__":
    run_calculator_repl()

