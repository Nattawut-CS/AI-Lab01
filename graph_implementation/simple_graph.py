def generate_edges(graph):
    edges = []
    for node in graph :
        for neighbour in graph[node] :
            edges.append((node, neighbour))
    return edges

graph = {
            'a' : ['c'],
            'b' : ['c', 'e'],
            'c' : ['a','b','d','e'],
            'd' : ['c'],
            'e' : ['c','b'],
            'f' : [] 
        }

# print(type(graph))
print(generate_edges(graph))