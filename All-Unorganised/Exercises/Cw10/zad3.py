"""
Wykonuje sortowanie topologiczne od wierzcholka s, bedzie on na poczatku sortowania topologicznego
nastepnie przechodzac po kolejnych wierzcholkach posortowanych topologicznych, dla kazdego z nich odwiedzam
jego sasiadow (ktorzy beda tylko na prawo w tej tablicy) i ustawiam najmnijesza mozliwa odleglosc jaka da sie tam dostac
"""

def shortest_paths( G, s ):

    n = len(G)
    visited = [False]*n
    top_sorted = []

    def top_dfs_visit( u ):
        nonlocal G, top_sorted, visited

        visited[u] = True

        for v, _ in G[u]:
            if not visited[v]:
                top_dfs_visit(v)

        top_sorted.append(u)


    top_dfs_visit(s)

    top_sorted = top_sorted[::-1]

    inf = float("inf")
    distance = [inf]*n
    distance[s] = 0

    for i in range( len(top_sorted) ):
        u = top_sorted[i]
        for v, cost in G[u]:
            distance[v] = min( distance[v], distance[u]+cost )

    return distance

