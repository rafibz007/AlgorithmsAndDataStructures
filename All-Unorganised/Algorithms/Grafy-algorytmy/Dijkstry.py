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

def Dijkstry2( G, s, t ):
    n = len(G)
    inf = float("inf")
    distance = [inf]*n
    done = [False]*n
    parent = [None]*n

    distance[s] = 0

    every_vertex_done = False
    while not every_vertex_done:

        u_min = t
        every_vertex_done = True
        for u in range(n):
            if not done[u] and distance[u_min] > distance[u]:
                every_vertex_done = False
                u_min = u

        if u_min == t: break
        if every_vertex_done: break

        u = u_min
        done[u] = True
        for v in range(n):
            if G[u][v] > 0 and distance[v] > distance[u] + G[u][v]:
                distance[v] = distance[u] + G[u][v]
                parent[v] = u

    return distance[t]


