import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def read_matrix():
    with open('data/input.txt', 'r') as f:
        matrix = [[int(num) for num in line.split(' ')] for line in f]
    return matrix


def draw_iconic_digraph(matrix):
    G = nx.DiGraph(matrix, name="Iconic digraph")
    pos = nx.random_layout(G)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    edge_labels = nx.get_edge_attributes(G, "weight")
    print(G.edges)
    nx.draw_networkx_edge_labels(G, pos, font_size=7, edge_labels=edge_labels)
    plt.show()


def main():
    matrix = np.matrix(read_matrix())
    draw_iconic_digraph(matrix)


if __name__ == "__main__":
    main()
