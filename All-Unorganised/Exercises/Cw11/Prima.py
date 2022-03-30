from queue import PriorityQueue

def prim( G ):
    inf = float("inf")
    n = len(G)

    weight = [inf]*n
    parent = [None]*n

    weight[0] = -inf

    Q = PriorityQueue()
    Q.put( (0, 0) )

    while not Q.empty():
        _, u = Q.get()
        for v,w in G[u]:
            if weight[v] > w:
                weight[v] = w
                parent[v] = u
                Q.put( (w, v) )

    print(parent)


G = [ [(1,5), (2,5), (3,8)],
      [(0,5), (2,8), (3,5)],
      [(0,5), (1,8), (3,5)],
      [(0,8), (1,5), (2,5)]]

print(prim(G))