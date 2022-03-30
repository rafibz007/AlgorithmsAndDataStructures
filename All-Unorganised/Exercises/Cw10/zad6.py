# Uzywam algo dijkstry wrzucajac do kolejki krotki
# ( <przejechane przez alicje>, <ostatni kierowca>, <wierzcholek docelowy> )
#
# odleglosc w kazdym wierzcholku bedzie przechowywana jako para
# d[u]=( <przejechane przez alicje gdy ostatnio jechala alicja>, <przejechane przez alicje gdy ostatnio jechal bob> )
#
# rodzicow w kazdym wierzcholku bede przechowywac rowniez jako krotke
# parent[u]=( <rodzic gdy ostatnio jechala alicja>, <rodzic gdy ostatnio jechal bob> )
#
# np teraz gdy wyciagne wierzcholek ( x, A, u ) i bede chcial pojechac do wierzcholka v
# to dorzuce do kolejki ( x, B, v ) pod warunkiem ze dokonam relaksacje
# a jesli ( x, B, u ), to wrzuce ( x+d(u,v), B, v )
#
# dokonywac relaksacji bede wtw, gdy idac z wierzchloka u do v: d[v][0] > d[u][1] + d(u,v)
# lub d[v][1] > d[u][0], oba te warunki bede rozpatrywac przy przegladaniu sasiadow wierzcholka wyciagnietego
# z kolejki i dla kazdego z nich bede wrzucac odpowiednie krotki do kolejki aktualizujac rodzicow
#
# zadziala to jak algorytm dijkstry dla dwoch osobnych instancji danego grafu
#
# Algorytm rozpoczynamy wrzucjac do kolejki 2 krotki
# ( 0, A, s )
# ( 0, B, s )
# ustawiajac odlegosc w tym wirzcholku na 0 w obu przypadkach
#
# wynik odczytac parentami i min odl latwo w wierzcholku t


from queue import PriorityQueue

def shortest_for_Alice( G, s, t ):

    A = 0
    B = 1

    n = len(G)
    Q = PriorityQueue()
    inf = float( "inf" )
    parent = [ [None, None] for _ in range( n ) ]
    distance = [ [inf, inf] for _ in range( n ) ]

    Q.put( (0, A, s) )
    Q.put( (0, B, s) )
    distance[s] = [0,0]

    while not Q.empty():
        Adist, last_driver, u = Q.get()
        # print(Adist, last_driver, u)

        if last_driver == A:
            for v,d in G[u]:
                # print("--", v, d, distance[v][B], distance[v][A] + d)
                if distance[v][B] > distance[u][A]:
                    # print("+")
                    distance[v][B] = distance[u][A]
                    parent[v][B] = u
                    Q.put( (Adist, B, v) )
        else:
            for v, d in G[u]:
                # print("--", v, d, distance[v][B], distance[v][A] + d)
                if distance[v][A] > distance[u][B] + d:
                    # print("+")
                    distance[v][A] = distance[u][B] + d
                    parent[v][A] = u
                    Q.put((Adist+d, A, v))

    # print(parent)
    # print(distance)
    path = [t]
    curr_driver = None

    if distance[t][A] < distance[t][B]: curr_driver = A
    else: curr_driver = B

    w = t
    while parent[w][curr_driver] is not None:
        w = parent[w][curr_driver]
        curr_driver = (curr_driver+1)%2 #zmiana na drugiego kierowce
        path.append(w)

    return path[::-1], min(distance[t]), "A" if (curr_driver+1)%2 == 0 else "B"

G = [ [(1,100), (2,100)],
      [(0,100), (2,1), (3,100)],
      [(0,100), (1,1), (3,100), (4, 10000)],
      [(1,100), (2,100)],
      [(2,10000), (5,1000)],
      [(4,1000)] ]

print( shortest_for_Alice(G, 0, 5) )