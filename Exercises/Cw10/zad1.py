"""
sortuje topologicznie wierzcholki, poczatek sciezki hamiltona musi znajdowac sie w pierwszym z posortowanych wierzcholkow
bo z nastepnych do niego nie wrocimy i sciezka bedzie nie pelna

w kazdym wierzcholku w posortowaniu topologicznym musi istniec krawedz do nastepnego z nich, poniewaz nie istnieja krawedzie w lewo
i przechodzac dalej nie wrocilibysmy do niego

czyli czy przy posortowaniu a b c, istnieja krawedzie (a,b), (b,c)
"""


def Hamilton(G):
    n = len(G)
    visited = [False] * n
    top_sorted = []

    def top_dfs_visit(u):
        nonlocal G, visited, top_sorted

        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                top_dfs_visit(v)

        top_sorted.append(u)

    for u in range( n ):
        if not visited[u]:
            top_dfs_visit(u)

    top_sorted = top_sorted[::-1]

    for i in range( n-1 ):
        if not top_sorted[i+1] in G[ top_sorted[i] ]:
            return False

    return True
