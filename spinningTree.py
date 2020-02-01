import networkx as nx
import matplotlib.pyplot as plt

G = nx.cycle_graph(4)
G.add_edge(0,3, weight=2)
tree = nx.minimum_spanning_tree(G)
print(sorted(tree.edges(data=True)))

nx.draw(G, with_labels = True)
plt.show()