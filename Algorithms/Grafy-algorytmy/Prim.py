from queue import PriorityQueue
def prim( G ):

    inf = float("inf")
    n = len(G)
    weight = [inf]*n
    parent = [None]*n

    Q = PriorityQueue()
    Q.put( (0,0) )
    weight[0] = inf

    while not Q.empty():
        _,u = Q.get()
        for v,w in G[u]:
            if weight[v] > w and parent[u] != v:
                weight[v] = w
                parent[v] = u
                Q.put( (w, v) )

    return parent