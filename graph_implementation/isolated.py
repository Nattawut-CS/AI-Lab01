def find_isolated_nodes(graph):
    isolated = []
    for node in graph :
        if not graph[node] :
            isolated += node
    return isolated

graph = {
            'a' : ['c'],
            'b' : ['c', 'e'],
            'c' : ['a','b','d','e'],
            'd' : ['c'],
            'e' : ['c','b'],
            'f' : [] 
        }

print(find_isolated_nodes(graph))