import networkx as nx
import matplotlib.pyplot as plt

g = nx.path_graph(5)
# path beginning at 0
p = nx.shortest_path(g, source=0)
p[4]

nx.draw(g, with_labels = True)
plt.show()