import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nx.add_path(G, [0,1,2])
tree = nx.dfs_tree(G,0)
print(tree.edges())

nx.draw(G, with_labels =True)
plt.show()