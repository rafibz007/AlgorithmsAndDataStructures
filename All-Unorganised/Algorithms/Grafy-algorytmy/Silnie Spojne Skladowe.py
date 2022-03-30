def list_to_matrix(G):
    n = len(G)
    GG = [[0] * n for _ in range(n)]

    for i in range(n):
        for v in G[i]:
            GG[i][v] = 1

    return GG


def print_2d( A ):
    for i in range( len(A) ):
        print(A[i])

#MACIERZ
def strong_complex( G ):
    def DFS_Visit( G, v ):
        nonlocal time, top_sorted, visited

        visited[v] = True

        time += 1
        for u in range( len(G) ):
            if not visited[u] and G[v][u]==1:
                DFS_Visit(G,u)

        time += 1
        top_sorted.append(v)

    def inverted_DFS_Visit( G, v, mark ):
        nonlocal visited, group

        visited[v] = True

        group[v] = mark
        for u in range(n):
            if not visited[u] and G[u][v] == 1:
                inverted_DFS_Visit(G,u,mark)


    n = len(G)
    top_sorted = []
    visited = [False]*n
    time = 0

    for v in range(n):
        if not visited[v]:
            DFS_Visit(G,v)

    group = [-1]*n
    visited = [False] * n
    top_sorted = top_sorted[::-1]

    mark = 0
    for v in top_sorted:
        if not visited[v]:
            inverted_DFS_Visit(G,v,mark)
            mark += 1

    return group


#LISTY SASIEDZTWA
def strong_complex2( G ):
    def invert_edges(G):
        n = len(G)
        invertedG = [[] for _ in range(n)]

        for u in range(n):
            for v in G[u]:
                invertedG[v].append(u)

        return invertedG

    def top_dfs_visit(u):
        nonlocal G, visited, top_sorted

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                top_dfs_visit(v)

        top_sorted.append(u)

    def dfs_visit(u):
        nonlocal invG, visited, group, curr_group

        group[u] = curr_group
        visited[u] = True
        for v in invG[u]:
            if not visited[v]:
                dfs_visit(v)


    n = len(G)
    visited = [False]*n
    group = [-1]*n
    top_sorted = []

    #posortwanie wierzcholkow po czasie przetworzenia malejaco
    for u in range(n):
        if not visited[u]:
            top_dfs_visit(u)

    top_sorted = top_sorted[::-1] #dla wygody, aby bylo malejaco
    for i in range(n): visited[i] = False

    #Obliczanie Silnie Spojnej Skladowej do ktore nalezy kazdy wierzcholek
    curr_group = 0
    invG = invert_edges(G)
    for u in top_sorted:
        if not visited[u]:
            dfs_visit(u)
            curr_group += 1

    return group



G = [[1,4],
     [2,3],
     [0,7],
     [4],
     [5],
     [3,6],
     [3],
     [9],
     [7],
     [10],
     [8]]

# print_2d( list_to_matrix(G) )
print( strong_complex(list_to_matrix(G)) )
print( strong_complex2(G) )