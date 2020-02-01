import networkx as nx
import matplotlib.pyplot as plt

# create an emtry graph
g = nx.Graph()

# ----------------- adding nodes to graph -----------------
# adding just one node (เพิ่ม 1 โหนด)
g.add_node('a')
# a list of nodes (เพิ่มโหนดแบบเป็นลิสต์, หลายโหนดทีเดียว)
g.add_nodes_from(['b', 'c'])
demoNodes = ['d', 'g']
g.add_nodes_from(demoNodes)
# ---------------------------------------------------

# ----------------- adding Edges to graph -----------------
# จับคู่ edges
g.add_edge(1, 2)
edgeNo1 = ('x', 'z') # type : tuple ()
edgeNo2 = ('p', 'q') # type : tuple ()
edgeNo3 = [('a', 'c'), ('c', 'd'), ('a', 1), (1, 'd'), ('a', 2)] # type : list []
# print(type(edgeNo3))
g.add_edge(*edgeNo1)
g.add_edge(*edgeNo2)
g.add_edges_from(edgeNo3)
# ---------------------------------------------------
print(f'nodes of graph : {g.nodes()}')
print(f'edges of graph : {g.edges()}')
nx.draw(g, with_labels = True)

# Save File
plt.savefig('path_graph.png')
plt.show()