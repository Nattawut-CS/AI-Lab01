import networkx as nx
import matplotlib.pyplot as plt

def dist(a, b):
    (x1, y1) = a 
    (x2, y2) = b
    return ((x1-x2)**2 +(y1-y2)**2)**0.5

G = nx.path_graph(5)
print(nx.astar_path(G, 0, 4))
# dim : 3*3 = 9
G = nx.grid_graph(dim=[3,3])

print(nx.astar_path(G, (0,0),(2,2),dist))
nx.draw(G, with_labels=True)
plt.show()
plt.savefig('a_path.png')