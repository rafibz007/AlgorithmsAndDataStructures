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


def strong_complex( G ):
    def DFS_Visit( G, v ):
        nonlocal time, done_time, visited

        time += 1
        for u in range( len(G) ):
            if not visited[u] and G[v][u]==1:
                visited[u] = True
                DFS_Visit(G,u)

        time += 1
        done_time[v] = [time,v]

    def inverted_DFS_Visit( G, v, mark ):
        nonlocal visited, group

        group[v] = mark
        for u in range(n):
            if not visited[u] and G[u][v] == 1:
                visited[u] = True
                inverted_DFS_Visit(G,u,mark)


    n = len(G)
    done_time = [-1]*n
    visited = [False]*n
    time = 0

    for v in range(n):
        if not visited[v]:
            DFS_Visit(G,v)

    group = [-1]*n
    visited = [False] * n
    done_time.sort(key=lambda x:x[0], reverse=True)

    mark = 0
    for _,v in done_time:
        if not visited[v]:
            inverted_DFS_Visit(G,v,mark)
            mark += 1

    # print(done_time)
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