
from queue import PriorityQueue
def Dijkstry( G, s, t ):

    n = len(G)
    inf = float("inf")
    distance = [inf]*n
    parent = [None]*n
    done = [False]*n
    Q = PriorityQueue()

    distance[s] = 0
    Q.put( (distance[s], s) )
    while not Q.empty():

        _,u = Q.get()
        if done[u]: continue
        done[u] = True

        for v,w in G[u]:
            #relaksacja
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                parent[v] = u
                Q.put( (distance[v], v) )

    return distance[t]
