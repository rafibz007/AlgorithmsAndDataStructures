"""
7.1

przeindeksowac na liczby naturalne i wykonac
f(i,j) - czy mozna stworzyc przedzial  [i,j]
f(i,j) = f(i,k) and f(k,j)  k - liczba z przedzialu (i,j)

f(i,j) = True jesli [i,j] jest dany

f(a,b) - odpowiedz

---

Traktuje to jako graf, w ktorym wierzcholkami sa przedzialy, a krawedz miedzy nimi itnieje gdy przedzial i konczy sie na to
czym zaczyna sie przedzial j

jesli dojde z wierzcholka zaczynajacego sie na a do wierzcholka konczacego sie na b, to sie da

#########
7.2

przeindeksowac na liczby naturalne i wykonac
f(i,j) - czy mozna stworzyc przedzial  [i,j]
f(i,j) = min(f(i,k) + f(k,j))  k - liczba z przedzialu (i,j)

f(i,j) = cost(i,j) jesli [i,j] jest dany

f(a,b) - odpowiedz

---

Traktuje to jako graf, w ktorym wierzcholkami sa przedzialy, a krawedz miedzy nimi itnieje gdy przedzial i konczy sie na to
czym zaczyna sie przedzial j, waga krawedzi jest cena wierzcholka do ktorego chce dojsc

algorytmem dijkstry staram sie dotrzec do przedzialu konczacego sie na b



#########
7.3

f(i,t) - najdluzszy przedzial jaki mozna uzyskac do i-tego z polaczenia t przedzialow
f(i,t) = max( f(i-1, t), f(i-j, t-1) + len(j) )

f(i,1) = len(i) jesli i jest dany

f(n-1, dowolne) - odp

---

Traktuje to jako graf, w ktorym wierzcholkami sa przedzialy, a krawedz miedzy nimi itnieje gdy przedzial i konczy sie na to
czym zaczyna sie przedzial j

Odpalam bfs dla kazdego wierzcholka i ide nim jedynie k-1 razy wglab, przy kazdym kroku obliczajac czy znalazlem
najwieksza odleglosc


"""
from collections import deque
from queue import PriorityQueue

def intervals1(T, a, b):

    n = len(T)
    visited = [False]*n
    Q = deque()

    for i in range(n):
        if T[i][0] == a:
            Q.append(T[i])


    while Q:

        interval = Q.popleft()
        if interval[1] == b:
            return True

        for i in range(n):
            if T[i] != interval and interval[1] == T[i][0] and not visited[i]:
                visited[i] = True
                Q.append(T[i])


    return False

def intervals2(T, C, a, b):
    n = len(T)
    inf = float("inf")
    cost = [inf] * n

    # mozna zaimplementowac bez kolejki przeszukujac tablice cost w celu znalezienia najmniejszego wierzcholka
    Q = PriorityQueue()

    for i in range(n):
        if T[i][0] == a:
            cost[i] = C[i]
            Q.put((cost[i], i))

    while not Q.empty():
        _, u = Q.get()
        interval = T[u]

        if interval[1] == b:
            return cost[u]

        for i in range(n):
            if T[i] != interval and interval[1] == T[i][0] and cost[i] > cost[u] + C[i]:
                cost[i] = cost[u] + C[i]
                Q.put((cost[i], i))

    return inf

def intervals3(T, k):

    n = len(T)
    inf = len(T)

    best_len = 0

    for i in range(n):
        visited = [False]*n
        distance = [inf]*n
        length = [-inf]*n

        Q = deque()

        distance[i] = 0
        length[i] = T[i][1]-T[i][0]
        Q.append(i)

        while Q:
            u = Q.popleft()
            interval = T[u]

            if distance[u] == k-1:
                continue

            for j in range(n):
                if T[j] != interval and interval[1] == T[j][0] and not visited[j]:
                    visited[j] = True
                    distance[j] = distance[u]+1
                    length[j] = length[u] + T[j][1]-T[j][0]
                    Q.append(j)

        # print(i,length,distance,visited)

        best_len = max( best_len, max(length) )

    return best_len



T = [  [-50, 3], [3,7], [6, 15], [20, 21], [10, 13], [7, 10], [9, 40], [13,20], [7,20]  ]
C = [        20,    12,       5,        7,       21,       8,       2,       6,      8  ]
print(intervals1(T,3,21))
print(intervals2(T,C,3,21))
print(intervals3(T,3))



