import networkx
import matplotlib.pyplot as plt

g = networkx.path_graph(5)
shortestPath = networkx.shortest_path(g, source=0, target=4)

print(shortestPath)

networkx.draw(g, with_labels = True)
plt.show()