import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import Utils as utls


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


def check_on_null_diagonal(matrix):
    u = True  # check on 0 diagonal
    for element in np.diagonal(matrix):
        if element != 0:
            u = False
            break
    return u


def check_balance(matrix):
    n = len(matrix)
    u = check_on_null_diagonal(matrix)

    if u:
        D = matrix + np.eye(N=n, dtype='double')  # adding ones matrix
    else:
        D = matrix

    DD = D.copy()
    W = []
    N = np.transpose(np.matrix([np.arange(0, n)]))
    WN = []

    while len(D) > 0:
        S = utls.get_sum(D > 0)
        S0, ii = utls.get_max(np.asarray(S))
        S1 = D * np.transpose(D[ii] > 0)
        B = S1 == np.transpose(S)
        N1 = np.hstack([N, B])
        k = []
        s = []
        raw = 0
        # deleting raws from matrix
        for i in B:
            if i:
                k.append(N1[raw, 0])
                s.append(raw)
            raw += 1

        D = np.delete(D, s, axis=0)
        W = utls.append_to_matrix(W, k)
        WN = utls.append_to_matrix(WN, k)
        WN = utls.append_to_matrix(WN, -(n - 1))
        N1 = np.delete(N1, k, axis=0)
        N = np.delete(N1, 1, axis=1)

    list_w = list(np.array(np.transpose(W)).reshape(-1, ))
    RESD = DD[np.ix_(list_w, list_w)]
    return W, RESD, WN


def main():
    matrix = np.matrix(read_matrix())
    draw_iconic_digraph(matrix)
    [W, DD, WN] = check_balance(matrix)
    list_wn = list(np.array(np.transpose(WN)).reshape(-1, ))
    list_w = list(np.array(np.transpose(W)).reshape(-1, ))
    print('W = ', list_w)
    print('DD = ', DD)
    print('WN = ', list_wn)
    DD[DD < 0] = 0
    print('DD = ', DD)


if __name__ == "__main__":
    main()
