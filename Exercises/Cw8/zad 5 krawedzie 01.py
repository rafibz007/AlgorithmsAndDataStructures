from collections import deque
from math import inf


def recursive_find( parents, s, t, solution, counter ):
    if s==t:
        solution.append(t)
    else:
        recursive_find(parents, s, parents[t], solution, counter)
        solution.append(t)
    return solution

#graf reprezentowany nastepujaco: -1 nie ma krawedzi, 0 krawedz o wadze 0, 1 krawedz o wadze 1;
#jesli jakas krawedz nie byla przez nas odwiedzona lub byla odwiedzona ale mozemy do niej tera dotrzec w lepszy sposob
#to trzeba ja rozpatrzec jeszcze raz; jesli poprawiajac lub idac do krawedzi przeszlismy po krawedzi o wadze 0
#to wkladamy wierzcholek do ktorego przyszlismy na poczatek kolejki, bo ponowne wywolanie go moze poprawic teraz nastepne wierzcholki
#a chcemy to zrobic od razu; jesli krawedz po ktorej przeszlismy ma wage 1, to odkladamy na koniec kolejki, aby najpierw
#poobliczac odpowiednie odleglosci miedzy wierzcholkami polaczonymi 0
def find_path( G, s, t ):
    n = len(G)
    dist = [inf]*n
    parent = [None]*n
    Q = deque()

    Q.append(s)
    dist[s] = 0

    while Q:
        u = Q.popleft()
        for v in range(n):
            if G[u][v] >= 0 and dist[v] > dist[u]+G[u][v]:
                dist[v] = dist[u]+G[u][v]
                parent[v] = u
                if G[u][v] == 0:
                    Q.appendleft(v)
                else:
                    Q.append(v)

    S = []
    counter = 0
    recursive_find(parent, s, t, S, counter)
    return S


g0 = [
        [-1, 1, -1, -1, -1, -1, 1, -1, -1],
        [-1, -1, 0, -1, 1, -1, -1, -1, -1],
        [-1, -1, -1, 0, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, 0, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, 1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 0],
        [-1, -1, -1, -1, -1, 0, -1, -1, -1]
    ]
print(find_path(g0, 0, 5))