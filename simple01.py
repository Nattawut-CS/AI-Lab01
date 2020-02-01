import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_node(1)
g.add_nodes_from([2,3])

h = nx.path_graph(10)
# add 10 nodes // h = 10 nodes
g.add_nodes_from(h)
# add 1 node // h = 11 nodes
g.add_node(h)

# set edge 1->2 connected
g.add_edge(1,2)

# 2->3
e = (2,3)
# set edge 2->3 connected
g.add_edge(*e)

# set edge 1->2, 1->3 connected
g.add_edges_from([(1,2), (1,3)])

# set all edge connected (h.edges)
g.add_edges_from(h.edges())
nx.draw(g, with_labels = True)
plt.show()