import networkx as nx
import matplotlib.pyplot as plt

# create 
g = nx.path_graph(4)
province ={0:'Bangkok', 1:'Pathumthani', 2:'pattaya', 3:'Ayutthaya'}

# rename nodes
h = nx.relabel_nodes(g, province)

print('nodes of graph : {}' .format(h.nodes))
print(f'edges of graph : {h.edges}')
# with_labels = show label of nodes (names)
nx.draw(h, with_labels = True)
plt.savefig('path_graph_province.png')
plt.show()