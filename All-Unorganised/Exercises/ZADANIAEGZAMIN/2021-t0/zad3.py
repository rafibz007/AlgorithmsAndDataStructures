"""
Nowy graf bedzie zbudowany z dwoch wersji z kazdego z wierzcholkow, jedna oznaczac bedzie, ze wchodzimy do niego
przechodzac przez 2 krawedzie, a druga ze przeslismy przez 1 krawedz

Implementacyjnie bede uzywac algorytmu dijksry na nowej wersji grafu ( ktora nie bedzie tworzona, bedzie jedynie
konceptem ), distans w kazdym wierzcholku bede trzymac jako para ( <odl gdy przyszedlem 1 krawedzia>, <2 krawedziami> )

W czasie O(2V) bede znajdywac wierzcholek ktory ma najmniejsza odleglosc od s, oraz zaczne go przetwarzac
relaksujac wszystkich jego sasiadow, a nastepnie sasiadow jego sasiadow w czasie O(V^2)

Relaksacji dokonywac bede, gdy moge dotrzec do danego wierzcholka, na dany sposob, szybciej niz wczesniej znalazlem
(uwzgledniam sytuacje gdy przyszedlem o 1 krok oraz 2 kroki osobno)

Wszystko wykonam dla kazdego wierzcholka, wiec zlozonosc wyniesie O(V^3)

"""

def jumper( G, s, w ):
    n = len(G)
    inf = float("inf")
    distance = [ [inf, inf] for _ in range(n) ]
    done = [ [False, False] for _ in range(n) ]
    parent = [ [None, None] for _ in range(n) ]

    distance[s] = [0,0]
    every_vertex_done = False
    while not every_vertex_done:

        u_min = w, 0
        every_vertex_done = True
        for u in range(n):
            if not done[u][0] and distance[u][0] < distance[u_min[0]][u_min[1]]:
                every_vertex_done = False
                u_min = u,0
            if not done[u][1] and distance[u][1] < distance[u_min[0]][u_min[1]]:
                every_vertex_done = False
                u_min = u,1

        if u_min[0] == w: break
        if every_vertex_done: break

        u = u_min
        done[u[0]][u[1]] = True

        #kroki o 1

        for v in range(n):
            if G[u[0]][v] > 0 and distance[v][0] > distance[u[0]][u[1]] + G[u[0]][v]:
                distance[v][0] = distance[u[0]][u[1]] + G[u[0]][v]
                parent[v][0] = u

        #kroki o 2

        if u[1] == 1: continue

        for v1 in range(n):
            if G[u[0]][v1] <= 0: continue
            for v2 in range(n):
                if G[v1][v2] <= 0: continue
                edge = max(G[u[0]][v1], G[v1][v2])

                if distance[v2][1] > distance[u[0]][0] + edge:
                    distance[v2][1] = distance[u[0]][0] + edge
                    parent[v2][1] = u


    # print()
    return min(distance[w])


G1 = [[0,1,0,0,0],
     [1,0,1,0,0],
     [0,1,0,7,0],
     [0,0,7,0,8],
     [0,0,0,8,0]]

G2 = [[0,19,10,0],
      [19,0,0,1],
      [10,0,0,11],
      [0,1,11,0]]

print(jumper(G1,0,4))
print(jumper(G2,0,3))