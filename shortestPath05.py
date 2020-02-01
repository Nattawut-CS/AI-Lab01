import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nx.add_path(G,[0,1,2])
nx.add_path(G,[0,10,2])

# for p in nx.all_shortest_paths(G, source=0, target=2):
    # print(p)

print([p for p in nx.all_shortest_paths(G, source=0, target=2)])

nx.draw(G, with_labels=True)
plt.savefig('shortestpath05.png')
plt.show()
