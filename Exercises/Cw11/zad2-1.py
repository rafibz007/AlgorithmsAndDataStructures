"""
Aby istniala sciezka zamknieta z danego wierzcholka spowrotem do niego, musi on nalezec do jakiejs silnie spojnej
skladowej, poniewaz jesli istnieje taka sciezka, to znaczy ze z wierzcholka s jestesmy w stanie dostac sie do wszystkich
wierzcholkow posrednich, a z nich jestesmy w stanie dostac sie do s, wiec jest to silnie spojna skladowa

Trasa wyscigu jesli wyjdzie poza silnie spojna skladowa, nie bedzie poprawna, bo nie bedzie mozliwosci powrotu do wierzcholka
startowego, bo jesli by byla, to calosc bylaby silnie spojna skladowa, a nie jest

W srodku silnie spojnej skladowej zawsze jestesmy w stanie stworzyc trase wyscigu przebiegajaca chociaz raz przez kazde
miasto nalezace do tej silnie spojnej skladowej (przy zalozeniu, ze wyscig moze przebiegac przez dana krawedz kilku krotnie -
czego tresc nie zabrania), zatem w kazdej silnie spojnej skladowej wybieramy trase wyscigu przechodzaca przez wszystkie jej
wierzcholki, dzieki czamu kazdy w niej wezmie udzial w dokladnie 1 wyscigu

Z tego wszystkiego wynika, ze w kazdej silnie spojnej skladowej mozna utworzyc wyscig(jesli nalezy do niej >1 wierzch),
ale z zadnej z nich nie mozemy wyjsc wybierajac trase, bo nie bedzie ona zamknieta

Zatem dziele graf na silnie spojne skladowe, i sprawdzam, czy kazda z nich zawiera conajmniej 2 wierzcholki, jesli tak to w kazdej
z nich bedzie trasa wyscigu i spelnimy warunki,
ale jesli w jakiejs nie bedzie 2 wierzcholkow, znaczy ,ze przez ten samotny wierzcholek nie jestesmy w stanie przeprowadzic
poprawnej trasy wyscigu

##########
wykonuje cos a'la sortowanie topologiczne aby ustawic wierzcholki po malejacym czasie przetworzenia
i latwiej wykonac przydzial grup silnych spojnych skladowych
"""

def invert_edges( G ):
    n = len(G)
    invertedG = [ [] for _ in range(n) ]

    for u in range( n ):
        for v in G[u]:
            invertedG[v].append(u)

    return invertedG


def racing( G ):

    def top_dfs_visit(u):
        nonlocal G, visited, top_sorted

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                top_dfs_visit(v)

        top_sorted.append(u)

    def dfs_visit(u):
        nonlocal invG, visited, vertex_scc_group, curr_group

        vertex_scc_group[u] = curr_group
        visited[u] = True
        for v in invG[u]:
            if not visited[v]:
                dfs_visit(v)


    n = len(G)
    visited = [False]*n
    vertex_scc_group = [-1]*n
    top_sorted = []

    #posortwanie wierzcholkow po czasie przetworzenia malejaco
    for u in range(n):
        if not visited[u]:
            top_dfs_visit(u)

    top_sorted = top_sorted[::-1] #dla wygody, aby bylo malejaco
    for i in range(n): visited[i] = False

    #Obliczanie Silnie Spojnej Skladowej do ktore nalezy kazdy wierzcholek
    curr_group = 0
    invG = invert_edges(G)
    for u in top_sorted:
        if not visited[u]:
            dfs_visit(u)
            curr_group += 1

    #obliczenie licznosci kazdej spojnej skladowej
    component_size = [0]*curr_group
    for u in range( n ): component_size[vertex_scc_group[u]] += 1

    # print(vertex_scc_group, component_size, top_sorted)

    for i in range( curr_group ):
        if component_size[i] == 1: return False


    return True


# G = [ [1],
#       [3],
#       [1],
#       [2],
#       [3,5],
#       [0],
#       [4,7],
#       [8],
#       [6]]

G = [ [1,4],
      [3],
      [1],
      [2],
      [3,5],
      [0],
      [4,7],
      [8],
      [6]]


print(racing(G))