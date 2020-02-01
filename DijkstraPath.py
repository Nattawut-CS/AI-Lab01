import networkx as nx
import matplotlib.pyplot as plt

G = nx.path_graph(5)

print(nx.dijkstra_path(G, 0, 4))

nx.draw(G, with_labels = True)
plt.savefig('DijkstraPath.png')
plt.show()