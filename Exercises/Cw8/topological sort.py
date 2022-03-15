

def topological_sort( G ):
    def DFS_Visit( G, v ):
        nonlocal visited, t_sorted

        for u in range( len(G) ):
            if G[v][u] == 1 and not visited[u]:
                visited[u] = True
                DFS_Visit( G, u )

        t_sorted.append( v )

    n = len(G)
    t_sorted = []
    visited = [False]*n
    for v in range( n ):
        if not visited[v]:
            visited[v] = True
            DFS_Visit(G, v)

    return t_sorted[::-1]


G = [[0,1,1,0,0,0,0,0,0],
     [0,0,1,0,1,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,1,0,1,1,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,1,0,0,0,0],
     [0,0,0,0,0,0,0,1,0]]

print(topological_sort(G))