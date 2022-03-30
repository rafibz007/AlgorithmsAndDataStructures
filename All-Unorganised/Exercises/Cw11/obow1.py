"""
Uzywam algorytmu dijkstry, wrzucajac do kolejki priorytetowej krotke
( <minimalny dystans>, <krawedz z ktorej przyszlismy>, <wierzcholek docelowy> )

Sortuje krawedzie dla kazdego wierzcholka po wagach i oznaczam je wszystkie jako nie odwiedzone

Dzieki temu rozpatrze wszystkie mozliwe przypadki wejscia do danego wierzcholka z danych poprzednikow

Z kolejki zawsze wyjdzie jako pierwszy wierzcholek o minimalnym dystansie, i tak jak w algorytmie dijkstry
Do wszystkich wierzcholkow do jakich damy rade dojsc obliczymy najmniejsza odleglosc

Do kazdego wierzcholka najpierw rozpatrzymy najszybsze sciezki aby sie do niego dostac i wejdziemy
do kazdej krawedzi do ktorej mozemy, zaznaczajac ze ja odwiedzilismy - mozemy tak zrobic, bo ta krawedz przez ktora
przejdziemy narzuci nam limit na nastepne odwiedzenie, wiec nie wazne czy ponownie wejdziemy do wierzcholka z wiekszej krawedzi
skoro z tego danego weszlismy z krotszej trasy

Po kazdym uzyciu krawedzi oznaczam je za odwiedzone i nie uzywam wiecej


w distance_parent zapisuje dla kazdego wierzcholka
( <dystans ktorym tu przyszedlem>, <krawedz po ktorej przyszedlem>, <rodzica> )
"""

from queue import PriorityQueue
from math import inf

def shortes_decreasing_path( G, s, t ):

    n = len(G)

    for i in range( n ): G[i].sort(reverse=True)

    distance_parent = [PriorityQueue() for _ in range(n)]

    Q = PriorityQueue()
    Q.put( ( 0, inf, s ) )

    while not Q.empty():
        dist, last_edge, u = Q.get()

        if u == t: continue

        for i in range( len(G[u])-1, -1, -1 ):
            v,w = G[u][i]
            G[u].pop()
            if last_edge > w:
                Q.put( ( dist+w, w, v ) )
                distance_parent[v].put( ( dist+w, w, u ) )


    _, last_edge, w = distance_parent[t].get()
    true_parent = None
    result = [t]

    while w != s:

        while not distance_parent[w].empty():
            parent = distance_parent[w].get()
            if parent[1] > last_edge:
                true_parent = parent
                break

        result.append(w)
        w = true_parent[2]
        last_edge = true_parent[1]



    result.append(s)
    return result[::-1]



G = [[(1,8),(2,7),(6,5)],
     [(0,8),(2,6),(3,5)],
     [(0,7),(1,6),(3,3),(4,8)],
     [(1,5),(2,3),(4,2),(5,4),(6,4)],
     [(2,8),(3,2),(5,3)],
     [(3,4),(4,3)],
     [(0,5),(4,4)]]

print(shortes_decreasing_path(G, 0, 5))