import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    P = [
        [0, 0.5, 0.3, 0.2],
        [0.1, 0.2, 0.55, 0.15],
        [0.4, 0.3, 0.2, 0.1],
        [0, 0.25, 0.35, 0.4]
    ]

    n = len(P)

    G = nx.DiGraph()

    for i in range(n):
        G.add_node(i)

    for i in range(n):
        for j in range(n):
            if P[i][j] > 0:
                G.add_edge(i, j, weight=P[i][j])

    pos = nx.spring_layout(G, seed=42, k=0.5)

    plt.figure(figsize=(8, 8))
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')
    nx.draw_networkx_edges(G, pos, width=2, arrowstyle='-|>', arrowsize=20)

    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Đồ thị chuỗi Markov")
    plt.axis('off') 
    plt.show()