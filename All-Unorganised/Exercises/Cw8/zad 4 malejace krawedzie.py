from collections import deque
from math import inf

def find_path( G, x, y ):

    n = len(G)
    last_edge = [-inf]*n
    parent = [None]*n

    Q = deque()
    Q.append(x)
    last_edge[x] = inf

    while Q:
        u = Q.popleft()
        if u == y:
            # print(last_edge)
            return True
        for v in range( n ):
            # krawedz istnieje and moge do niej isc bo poprzednia krawedz byla wieksza and znalazlem lepsza sciezke gdzie mam wieksza poprz
            #krawedz wiec oplaca sie wejsc i z uptadetowac
            if G[u][v] != 0 and last_edge[u]>G[u][v] and last_edge[v]<G[u][v]:

                parent[v] = u
                last_edge[v] = G[u][v]
                Q.append(v)

    return False


g0 = [
        [0, 1, 0, 7, 0, 0, 0],
        [1, 0, 2, 3, 0, 10, 0],
        [0, 2, 0, 5, 0, 11, 0],
        [7, 3, 5, 0, 8, 0, 0],
        [0, 0, 0, 8, 0, 4, 0],
        [0, 0, 11, 0, 4, 0, 6],
        [0, 0, 0, 0, 0, 6, 0]
    ]
# z 1 do 5 True
print(find_path(g0, 1, 5))
# z 5 do 1 True
print(find_path(g0, 5, 1))
# z 6 do 3 False
print(find_path(g0, 6, 3))
# z 4 do 0 True
print(find_path(g0, 4, 0))
# z 4 do 2 True
print(find_path(g0, 4, 2))
# z 6 do 0 False
print(find_path(g0, 6, 0))