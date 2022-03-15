def binsearch( T, val ):
    top = len(T)-1
    bot = 0

    while bot <= top:
        mid = (top+bot)//2
        if T[mid] > val: top = mid-1
        elif T[mid] < val: bot = mid+1
        else: return True

    return False
#VlogV - sortowanie listy krawedzi max V jego sasiadow dla kazdego wierzcholka
#ElogV - dla kazdej krawedzi zadanej w liscie wykonujemy wyszukiwanie biarne na max V elem
#O(VlogV + ElogV)
def check_if_directed( G ):
    n = len(G)
    for i in range(n): G[i].sort()

    for u in range(n):
        for v in G[u]:
            if not binsearch( G[v], u ): return False

    return True


G = [ [1, 2],
      [0, 2],
      [0,1],
      [4,6],
      [3,5],
      [4,6],
      [3],
      []
]
print(check_if_directed(G))