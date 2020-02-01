import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nx.add_path(G, range(0,51))
print(list(nx.bfs_edges(G,0)))

nx.draw(G, with_labels=True)
plt.show()