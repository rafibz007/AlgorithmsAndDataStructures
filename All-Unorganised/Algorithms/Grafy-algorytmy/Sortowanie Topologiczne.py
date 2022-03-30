def topological_sort( G ):
    def dfs_visit( u ):
        nonlocal G, visited, result

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(v)

        result.append(u)


    n = len(G)
    visited = [False]*n
    result = []

    for u in range(n):
        if not visited[u]:
            dfs_visit(u)

    return result[::-1] #lub result, w sumie nw