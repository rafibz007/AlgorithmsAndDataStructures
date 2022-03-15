"""
wartosc a*b bedzie maksymalna bedzie gdy wartosc log2(a*b) bedzie maksymalna
log2(a*b) = log2(a) + log2(b)
zatem z ta wlasnoscia mozna zastosowac algorytm dijkstry, obliczajac odleglosc jako logarytm z niej

"""


from math import log2, inf
from queue import PriorityQueue



def Dijkstry( G, s, t ):

    n = len(G)
    Q = PriorityQueue()
    distance = [inf]*n
    done = [False]*n
    parent = [None]*n

    Q.put( (0,s) )
    distance[s]=0
    done[s]=True

    while not Q.empty():
        _,u = Q.get()
        if done[u]: continue
        done[u] = True

        for v,w in G[u]:
            w = log2(w)
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                parent[v] = w
                Q.put( ( distance[v], v ) )


    result = [t]
    u = t
    while u != s:
        u = parent[u]
        result.append(u)

    return result
