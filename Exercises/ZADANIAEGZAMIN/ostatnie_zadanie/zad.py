from zad2testy import runtests
from queue import PriorityQueue


def let(ch): return ord(ch) - ord("a")


def list_of_edges_to_list(E, n):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append([edge[1],edge[2]])
        G[edge[1]].append([edge[0],edge[2]])

    return G

"""
kazdy wierzcholek grafu rozbijam na <dlugosc slowa instancji> oraz lacze odpowiednio krawedziami
te wierzcholki, tak aby kazdy prowadzil tylko do wierzcholka oznaczajacego dlugosc wieksza oraz
aby wierzcholek docelowy posiadal ospowiednia literke

implementacyjnie tworze tablice distance [vertex_amount][word_len] i uzywajac algorytmu dijkstry
wrzucamd o kolejki krotki (dystans, dlugosc slowa, cel) i dokouje relaskacji tylko gdy dystans
do danego wierzcholka przy danej dlugosci jest wiekszy niz moglibysmy go teraz osiagnac

Gdy po raz pierwszy wyciagne docelowy wierzcholek (czyli taki, gdzie dlugosc slowa wynosi juz word_len,
to moge zwrocic dystans jakim przybyl, bo na pewno jest to najszybciej jak sie dalo)

"""


def letters(G, W):
    L, E = G
    vertex_amount = len(L)
    word_length = len(W)
    G = list_of_edges_to_list(E, vertex_amount)

    inf = float("inf")
    distance = [ [inf]*(word_length+1) for _ in range(vertex_amount) ]

    Q = PriorityQueue()
    for v in range(vertex_amount):
        if L[v] == W[0]:
            distance[v][1] = 0
            Q.put( (0, 1, v) )

    while not Q.empty():
        dist, curr_len, u = Q.get()

        if curr_len == word_length:
            return dist

        for v,w in G[u]:
            if L[v] != W[curr_len]: continue
            if distance[v][curr_len+1] > distance[u][curr_len] + w:
                distance[v][curr_len+1] = distance[u][curr_len] + w
                Q.put( (distance[v][curr_len+1], curr_len+1, v) )

    return -1


runtests(letters)


