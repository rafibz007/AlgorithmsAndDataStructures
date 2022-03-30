from collections import deque
def path( G, s, t ):
    n = len(G)
    visited = [-1]*n
    parent = [-1]*n

    Q = deque()
    Q.append(s)
    visited[s] = 0

    P = []

    while Q:
        u = Q.popleft()
        if u == t:
            dist = visited[u]
            w = u
            P.append(w)
            for _ in range(dist):
                w = parent[w]
                P.append(w)
            return dist, P[::-1]
        for v in G[u]:
            if visited[v] < 0: #if not visited
                visited[v] = visited[u] + 1
                Q.append(v)
                parent[v] = u

    return -1


g0 = [
        [1],
        [0,2,4],
        [1,3,5],
        [2,4],
        [1,3,6],
        [2,7],
        [4,7],
        [6,5]
    ]
print(path(g0, 7, 2))