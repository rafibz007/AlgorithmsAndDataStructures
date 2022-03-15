"""
wykonuje cos a'la sortowanie topologiczne, dopuszczajac krawedzie w lewo w silnie spojnych skladowych
w ten sposob na poczatku posortowanych wierzcholkow, znajdzie sie jeden z wierzcholkow silnie spojnej skladowej
ktora, po posortowaniu ich topologicznie bylaby pierwsza, sprawdzam czy z tego wierzcholka da sie dotrzec wszedzie
jesli tak to go zwracam, jesli nie, to taki nie istnieje

bedzie tak bo przy sortowaniu topologicznym taki wierzcholek bedzie mial najwiekszy czas przetworzenia (a tak szukalismy
kolejnych silnie spojnych skladowych) czyli stworzy pierwsza silnie spojna skladowa posiadajaca tylko krawedzie w prawo
"""

def good_beginnig( G ):
    def top_DFS_Visit( u ):
        nonlocal visited, G, topological_sorted

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                top_DFS_Visit(v)

        topological_sorted.append(u)


    def DFS_Visit( u ):
        nonlocal visited, G

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_Visit( v )


    n = len(G)
    visited = [False]*n
    topological_sorted = []

    for u in range( n ):
        if not visited[u]:
            top_DFS_Visit(u)

    topological_sorted = topological_sorted[::-1]

    for i in range(n): visited[i]=False
    DFS_Visit( topological_sorted[-1] )

    for u in range(n):
        if not visited[u]: return False

    return topological_sorted[-1]


