def kruskal(graph):
    edges = []
    for v in graph:
        for u, w in graph[v]:
            edges.append((w, v, u))
    
    edges.sort()
    
    sets = {}
    for v in graph:
        sets[v] = v
    
    mst = []
    
    for w, v1, v2 in edges:
        root1 = find(sets, v1)
        root2 = find(sets, v2)
        
        if root1 != root2:
            mst.append((v1, v2, w))
            sets[root2] = root1
    
    total_weight = sum(w for v1, v2, w in mst)
    
    return mst, total_weight

def find(sets, v):
    if sets[v] != v:
        sets[v] = find(sets, sets[v])
    return sets[v]

# Example usage
graph = {
    'A': [('B', 5), ('D', 4)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 6)],
    'D': [('B', 2), ('A', 4)]
}

mst, total_weight = kruskal(graph)
print("Minimum spanning tree (MST):")
for u, v, weight in mst:
    print("{} - {} : {}".format(u, v, weight))
print("Total Weight:", total_weight)