from collections import deque
#DWUDZIELNY
#RED - 0
#BLUE - 1

#lista krawedzi
def dwudzielny( G ):
    Q = deque()

    color = [ -1 ]*len(G)
    parent = [ -1 ]*len(G)
    c = 0
    for w in range( len(G) ):
        if color[w] == -1: #znaczy ze nie odwiedzony
            Q.append(w)
            color[w] = c
        while Q:
            c = (c+1)%2
            u = Q.popleft()
            for v in G[u]:
                if parent[u] == v: continue
                if color[v] == -1: color[v] = c
                elif color[v] != c: return False
                else: continue
                Q.append(v)
                parent[v] = u

    # print( color, parent )
    return True

G = [ [2],
      [2,4],
      [0,1,3],
      [2,5],
      [1],
      [3],
      []
]
print(dwudzielny(G))

#USUWANIE WIRZCHOLKOW
def bridges( G ):

    def DFS_Visit( G, v ):
        nonlocal time, visited, visit_time, parent, low

        time += 1
        visit_time[v] = time
        visited[v] = True
        low[v] = time

        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                parent[u] = v
                DFS_Visit( G, u )
                low[v] = min( low[v], low[u] )
            elif parent[v] != u:
                low[v] = min( low[v], low[u] )

        time += 1


    n = len(G)
    visited = [False]*n
    visit_time = [-1]*n
    parent = [-1]*n
    low = [-1]*n
    time = 0
    for v in range(n):
        if not visited[v]:
            DFS_Visit( G, v )

    B = []
    for v in range(n):
        if visit_time[v] == low[v] and parent[v] != -1:
            B.append( [parent[v], v] )

    return B

def delete_path( G, S ):

    def DFS_Visit( G, v ):
        nonlocal visited, found_bridges, S

        visited[v] = True

        # jesli moge przechodze przez most i rozpatruje najpierw co za nim
        for b in range(len(found_bridges)):
            if found_bridges[b][0] == v:  # czy v jest wierzcholkiem mostu
                if not visited[ found_bridges[b][1] ]:
                    DFS_Visit(G, found_bridges[b][1])

        for u in G[v]:
            if not visited[u]:
                DFS_Visit( G, u )

        S.append( v )


    n = len(G)
    visited = [False]*n
    found_bridges = bridges(G)

    DFS_Visit( G, 0 )
    return S


def bridges2( G ):

    def DFS_Visit( G, v ):
        nonlocal time, visited, parent, visited, low

        time += 1
        visited[v] = True
        visit_time[v] = time
        low[v] = time

        for u in range( len(G) ):
            if G[v][u] == 1:
                if not visited[ u ]:
                    parent[u] = v
                    DFS_Visit( G, u )
                    low[v] = min( low[v], low[u] )
                elif parent[v] != u:
                    low[v] = min(low[v], low[u])
        time += 1

    n = len(G)
    time = 0
    visited = [False]*n
    parent = [None]*n
    visit_time = [-1]*n
    low = [-1]*n

    DFS_Visit(G, 0)

    for v in range( n ):
        if visit_time[v] == low[v] and parent[v] is not None:
            G[ v ][ parent[v] ] += 1
            G[ parent[v] ][ v ] += 1

def delete_path2( G, S ):

    def DFS_Visit( G, v ):
        nonlocal visited, S

        visited[v] = True

        for u in range( len(G) ):
            if G[v][u] > 1 and G[u][v] > 1: #znaczy ze istnieje most miedzy tymi krawedziami
                if not visited[u]:
                    G[v][u] -= 1
                    G[u][v] -= 1
                    DFS_Visit( G, u )

        for u in range( len(G) ):
            if G[v][u] == 1:
                if not visited[u]:
                    DFS_Visit( G, u )

        S.append( v )

    n = len(G)
    visited = [False]*n
    bridges2(G)

    return S

# G = [ [1, 2],
#       [0, 2],
#       [0,1,3],
#       [2,4,6],
#       [3,5,7],
#       [4,6],
#       [3,5],
#       [4]
# ]
G = [[0,1,1,0,0,0,0,0],
     [1,0,1,0,0,0,0,0],
     [1,1,0,1,0,0,0,0],
     [0,0,1,0,1,0,1,0],
     [0,0,0,1,0,1,0,1],
     [0,0,0,0,1,0,1,0],
     [0,0,0,1,0,1,0,0],
     [0,0,0,0,1,0,0,0]]
print(bridges2(G))