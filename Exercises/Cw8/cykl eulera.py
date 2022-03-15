from collections import deque


# zamiast kopiowac macierz G sprawdzam czy wierzcholek zostal przerobiony na podstawie ostatniego wierzcholka jaki odwiedzil
# bo to znaczy ze wszystkie mniejsze badz rowne tej wartosci zostaly juz odwiedzone i te krawedzie nie istnieja

def euler(G):
    def DFS_Visit(G, v):
        nonlocal path, last_visited #,Q

        # Q.append(v)
        leave_vertex[v] += 1
        for u in range(last_visited[v] + 1, len(G)):
            last_visited[v] += 1
            # last_visited[u]+1 <= v wtw gdy wierzcholek u nie zdazyl podczas swojej iteracji osiagnac v, wiec teraz mozemy isc z u do v
            if G[v][u] == 1 and last_visited[u] + 1 <= v:
                DFS_Visit(G, u)

        # jesli tyle razy wszedlem do wierzcholka ile wyszedlem to leave_vertex bedzie rowny 0
        # jesli bedzie wiekszy od 0 na koniec programu, znaczy ze nie znaleziono cyklu eulera i gdzies sie zatrzymalismy
        leave_vertex[v] -= 1

        path.append(v)
    n = len(G)
    path = []
    last_visited = [-1] * n
    leave_vertex = [0] * n

    DFS_Visit(G, 0)

    # min(last_visited) == -1 wtw gdy z wierzcholka 0 nie dostalismy sie do wierzcholka v, czyli graf jest niespojny
    # min(leave_vertex) != 0 or max(leave_vertex) != 0 wtw gdy z jakiegos wierzcholka nie wyszlismy tyle razy ile weszlismy, wiec nie ma cyklu
    if min(leave_vertex) != 0 or max(leave_vertex) != 0 or min(last_visited) == -1: return None
    return path


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

GG = G
cycle = euler(G)
print(cycle)

if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == 0:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = 0
    GG[v][u] = 0
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == 1:
            print("Błąd (3)!")
            exit(0)

print("OK")