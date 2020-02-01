import networkx as nx
import matplotlib.pyplot as plt

G = nx.path_graph(50)

p = nx.shortest_path(G, target=41)
p[0]

nx.draw(G, with_labels = True)
plt.show()