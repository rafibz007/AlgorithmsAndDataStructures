#LISTY SASIEDZTWA
def Bellman_Ford( G, s, t ):
    n = len(G)
    inf = float("inf")
    distance = [inf] * n
    parent = [None] * n
    distance[s] = 0

    for i in range(n):
        for u in range(n):
            for v,w in G[u]:
                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    parent[v] = u

    for u in range(n):
        for v,w in G[u]:
            if distance[u] + w < distance[v]: return None

    return distance[t]