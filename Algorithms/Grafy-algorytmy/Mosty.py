def bridges(G):
    def DFS_Visit(G, v):
        nonlocal time, visited, visit_time, parent, low

        time += 1
        visit_time[v] = time
        visited[v] = True
        low[v] = time

        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                parent[u] = v
                DFS_Visit(G, u)
                low[v] = min(low[v], low[u])
            elif parent[v] != u:
                low[v] = min(low[v], low[u])

        time += 1

    n = len(G)
    visited = [False] * n
    visit_time = [-1] * n
    parent = [-1] * n
    low = [-1] * n
    time = 0
    for v in range(n):
        if not visited[v]:
            DFS_Visit(G, v)

    B = []
    for v in range(n):
        if visit_time[v] == low[v] and parent[v] != -1:
            B.append([parent[v], v])

    return B