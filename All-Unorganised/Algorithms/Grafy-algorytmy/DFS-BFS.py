from collections import deque


def bfs(G, s, t):
    n = len(G)
    inf = float("inf")
    distance = [inf] * n
    visited = [False] * n
    distance[s] = 0

    Q = deque()

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                Q.append(v)

    return distance[t]


def dfs( G ):

    def dfs_visit(u):
        nonlocal G, visited, time

        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(v)

        time += 1

    n = len(G)
    visited = [False] * n
    time = 0
    for u in range(n):
        if not visited[u]:
            dfs_visit(u)

