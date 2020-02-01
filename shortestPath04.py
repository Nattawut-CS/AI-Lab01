import networkx as nx
import matplotlib.pyplot as plt

G = nx.path_graph(100)

p = nx.shortest_path(G)
p[4][76]

nx.draw(G, with_labels = True)
plt.show()