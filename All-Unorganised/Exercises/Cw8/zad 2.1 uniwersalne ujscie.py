from collections import deque

def universal_exit( G ):
    n = len(G)
    Q = deque()
    result = False
    for v in range( n ):
        if sum(G[v]) == 0: #czyli jesli z wierzcholka v nie wychodzi zadna krawedz
            visited = [False] * n
            Q.append( v )
            visited[v] = True

            while Q:
                u = Q.popleft()
                # indeksy sa odwrocone, bo odwracam krawedzie grafu i probuje w ten sposob dotrzec wszedzie
                for w in range(n):
                    if G[w][u] > 0 and not visited[w]:
                        visited[w] = True
                        Q.append(w)

            for i in range(n):
                if not visited[i]: continue

            result = v
            break

    return result



g0 = [
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0]
    ]
print(universal_exit(g0))