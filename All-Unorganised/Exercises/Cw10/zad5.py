"""
Wykonuje zmodyfikowany algorytm Dijkstry, wykonujacy relaksjacje gdy dam rade dotrzec do danego wierzcholka
wieksza krawedzia niz doszlismy poprzednio

Kolejka sortuje od najmnijeszych, a nie znam innej XD, wiec wkladam do niej wartosci ( -<przepustowosc>, <cel> )
aby wyciagala najpierw wierzcholki ktore gwarantuja najwieksza przepustowosc aby sprawdzac je wczesniej
Dzieki temu otrzymamy znacznie mniej relaksacji, bo otrzymamy od razu najlepsze wyniki w wielu wierzcholkach

"""

from queue import PriorityQueue

def count_groups( E,s,t,k ):
    amount_of_v = 0
    for i in range( len(E) ): amount_of_v = max( amount_of_v, E[i][0], E[i][1] )
    amount_of_v += 1

    n = amount_of_v
    G = [ [] for _ in range(n) ]
    for i in range( len(E) ): G[ E[i][0] ].append( ( E[i][1], E[i][2] ) )

    inf = float("inf")
    lowest_edge = [0]*n
    parent = [None]*n

    Q = PriorityQueue()
    Q.put( (-inf, s) )
    lowest_edge[s] = inf

    while not Q.empty():
        cap, u = Q.get()
        cap = -cap #to przyjecie mojej dziwnej konwencji XD

        for v, d in G[u]:
            if lowest_edge[v] < min( cap, d ):
                lowest_edge[v] = min( cap, d )
                parent[v] = u
                Q.put( (-lowest_edge[v], v) )


    # print(parent, lowest_edge)
    best_cap = lowest_edge[t]
    return k//best_cap if k%best_cap == 0 else k//best_cap+1


E = [(0, 1, 10), (1, 2, 8),(1, 3, 4), (1, 4, 3), (2, 5, 2), (3, 5, 4), (4, 5, 10)]
print(count_groups(E, 0, 4, 14))