# G - macierz sasiedztwa (0 znaczy ze krawedzi nie ma)
# flow[u][v] to przeplyw jaki mamy z u do v, a flow[v][u] to przeplyw zwrotny
from queue import PriorityQueue
def max_flow( G, s, t ):
    n = len(G)
    flow = [ [0]*n for _ in range(n) ]
    inf = float("inf")

    flow_max = 0
    while True:
        parent = [None]*n
        Q = PriorityQueue()
        Q.put(s)

        while not Q.empty():
            u = Q.get()
            for v in range(n):
                if u == v: continue
                cap = G[u][v] - flow[u][v]
                if parent[v] is None and cap > 0:
                    parent[v] = u
                    Q.put(v)


        #jesli nie znaleziono przeplywu powiekszajacego
        if parent[t] is None: break

        new_flow = inf
        w = t
        while w != s:
            new_flow = min( new_flow, G[parent[w]][w] - flow[parent[w]][w] )
            w = parent[w]

        w = t
        while w != s:
            flow[parent[w]][w] += new_flow
            flow[w][parent[w]] -= new_flow
            w = parent[w]

        flow_max += new_flow

    return flow_max



def list_to_matrix( G ):
    n = len(G)
    GG = [ [0]*n for _ in range(n) ]

    for i in range(n):
        for v,w in G[i]:
            GG[i][v]=w

    return GG
#
# G1 = [[(1,1), (5,1)],
#      [(2,1)],
#      [(3,1)],
#      [],
#      [(3,1)],
#      [(2,1), (4,1)]]
#
G2 = [[(1,3), (6,3), (5,4)],
      [(2,2)],
      [(3,2), (5,1)],
      [],
      [(3,5)],
      [(4,5)],
      [(2,1), (1,10)]]
#
# print(list_to_matrix(G1))
print(list_to_matrix(G2))
# print(max_flow(list_to_matrix(G1), 0, 3))
print(max_flow(list_to_matrix(G2), 0, 3))