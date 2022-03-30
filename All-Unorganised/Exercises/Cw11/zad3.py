"""
Tworze graf, z podanych danych, gdzie wierzcholki to waluty, a krawedzie to podany kurs

Jesli zmienimy znaczneie krawedzi nastepujaco: zmiast oznaczac ile trzeba dac x aby otrzymac 1y, bedzie ile y dostaniemy za 1x
(odpowiadaloby to zmianie kazdej d(u,v) = 1/(d(u,v)))
to w prosty sposob mozna sprawdzic co sie stanie jesli wrzucimy jedna np zlotowke do obiegu.
Chcemy osiagnac sytuacje w ktorej wroci do nas wartosc wieksza od 1, bo to oznacza ze udalo nam sie zarobic

Aby uzyc algorytmu Bellmana Forda nie moge wykonywac mnozenia krawedzi, ale dodawnie, wiec zamieniam
kazda krawedz: d(u,v) = log(d(u,v)). Teraz chce aby wykryl on cykl gdy a>1, czyli gdy loga>0
Bellman Form wykrywa jedynie ujemne cykle, wiedz zmieniam kazda krawedz d(u,v) = -d(u,v), aby znajdowal mi teraz te dodatnie

Wiec po 3 kolejnych przeksztalceniach:
    d(u,v) = 1/(d(u,v))
    d(u,v) = log(d(u,v)
    d(u,v) = -d(u,v)

otrzymamy finalnie sytuacje w ktorej wykonalibysmy tylko jedno przeksztalcenie
d(u,v) = log(d(u,v)

Teraz tworze graf, wykonuje przerobke krawedzi d(u,v) = log(d(u,v)), oraz wykonuje algorytm Bellmana Forda
na dowolnym wierzcholku, ktory wykryje mi cykle ktore dadza mi zysk (poniewaz jesli taki cykl istnieje to na pewno do niego
dojde i go wykryje, wiec nie musze puszczac dla wszystkich)
"""


from math import log2

def change( G ):

    n = len(G)

    for x in range(n):
        for y in range(n):
            if x == y or G[x][y] is None: continue
            G[x][y] = log2(G[x][y])


    inf = float("inf")
    distance = [inf]*n
    parent = [None]*n
    distance[0] = 0

    for i in range( n-1 ):
        for x in range(n):
            for y in range(n):
                if x == y or G[x][y] is None: continue
                if distance[y] > distance[x] + G[x][y]:
                    distance[y] = distance[x] + G[x][y]
                    parent[y] = x

    # print(parent)
    for x in range(n):
        for y in range(n):
            if x == y or G[x][y] is None: continue
            if distance[x] + G[x][y] < distance[y]: return True

    return False

K1 = [
    [None, 4.50, 8, None],
    [None, None, 2, None],
    [None, None, None, 0.005],
    [0.2, None, None, None]
]
print(change(K1))
K2 = [
    [None, 4.50, None, 4],
    [None, None, 2, None],
    [None, None, None, 5],
    [1.2, 8, None, None]
]
print(change(K2))