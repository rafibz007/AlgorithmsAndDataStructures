"""
Szukany wierzcholek musi byc na srednicy grafu, poniewaz na jej srodku odleglosc do skrajnych krawedzi
bedzie wynosic conajmniej dlugosc/2, a odleglosc do pobocznych galezi bedzie mniejsza i nie bedzie odgrywac roli

Obliczam srednice grafu poprzez dwukrotne wywolanie algorytmu dijkstry, pierwszy raz na dowolnym wierzcolku, a drugi
raz na wierzcholku ktory byl od tego najdalej. Znajde w ten sposob srednice, poniewaz:
    jesli wywolamy za pierwszym razem dijkstre na dowolnym wierzcholku to wykona ona jakas droge to srednicy (mniejsza niz
    droga po obu stronach tego pkt dolaczenia do srednicy) oraz dotrze do jej najlaszego wierzcholka
    w ktorym osiagnie maksymalna odleglosc, poniewaz
    odnogi ktore zbaczaja w bok maja dlugosc krotsza niz kazda ze stron tej srednicy w tym pkt

Wywolujac algorytm drugi raz, znajduje cala srednice w analogiczny sposob, najladel pkt startowy
bedzie miec do drugiego konca srednicy

przechodzac po srednicy szukam pkt w ktorym odleglosc od lewego konca i prawego bedzie minimalna

W zasadzie to chyba zamiast dijkstry mozna uzyc zwyklego bfsa, bo i tak nigdy nie bedziemy relaksowac nic
zwraca te same wyniki :))
"""

from collections import deque


def matrix_to_list(G):
    n = len(G)

    W = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if G[u][v] > 0:
                W[u].append((v, G[u][v]))

    return W


def minimal( G ):

    def bfs( s ):
        nonlocal G, n, distance, parent

        Q = deque()
        Q.append( s )
        distance[s] = 0

        while Q:
            u = Q.popleft()
            for v,w in G[u]:
                if distance[v] > distance[u] + w: #if visited
                    parent[v] = u,w
                    distance[v] = distance[u] + w
                    Q.append( v )


    n = len(G)
    inf = float("inf")
    distance = [inf]*n
    parent = [None]*n

    bfs(0)

    left_v = 0
    for i in range( 1,n ):
        if distance[left_v] < distance[i]: left_v = i

    distance = [inf] * n
    parent = [None] * n

    bfs(left_v)

    right_v = 0
    for i in range(1, n):
        if distance[right_v] < distance[i]: right_v = i

    value_left = distance[right_v]
    value_right = 0

    min_distance = [inf]*n
    min_distance[left_v] = value_left

    # print(parent, right_v)

    w = right_v
    while parent[w] is not None:
        # print(w)
        min_distance[w] = max( value_left, value_right )
        value_right += parent[w][1]
        value_left -= parent[w][1]
        w = parent[w][0]

    best = 0
    for i in range(1, n):
        if min_distance[best] > min_distance[i]: best = i

    # print(min_distance)

    return best


T1 = [[(1, 1)],
     [(0, 1), (2, 1)],
     [(1, 1), (3, 1), (4, 1)],
     [(2, 1)],
     [(2, 1), (5, 1), (6, 1), (8, 1)],
     [(4, 1)],
     [(4, 1), (7, 1)],
     [(6, 1)],
     [(4, 1), (9, 1), (10, 1)],
     [(8, 1)],
     [(8, 1)]]

print(minimal(T1))
T2 = [[(3, 1000)],
      [(3, 1)],
      [(3, 1), (4, 1)],
      [(0, 1000), (1, 1), (2, 1), (5, 1)],
      [(2, 1)],
      [(3, 1), (6, 1)],
      [(5, 1)]]

print(minimal(T2))