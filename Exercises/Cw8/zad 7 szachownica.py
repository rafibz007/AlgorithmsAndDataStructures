from math import inf
from collections import deque
from random import randint

def print_2d( A ):
    for i in range(len(A)):
        print(A[i])

def rec_print( A, P, i, j, sum ):
    if i == 0 and j == 0:
        print( f"({j},{i};{A[i][j]})", end=' ' )
        return A[i][j]
    else:
        s = rec_print( A, P, P[i][j][0], P[i][j][1], sum )
        print(f"({j},{i};{A[i][j]})", end=' ')

    return s + A[i][j]

#uzywam stosu
#jesli moge polepszyc dojscie do jakiegokolwiek wierzcholka to polepszam je i wrzucam go na stos
#aby polepszony wierzcholek mogl polepszyc wszystkich swoich gorszych sasiadow, w ten sposob otrzymamy
#najlepsze drogi do kazdego pola z 0,0
def kings_path( A ):
    n = len(A)
    dist = [[inf]*n for _ in range(n)]
    parent = [[None]*n for _ in range(n)]

    dist[0][0] = A[0][0]

    Q = deque()
    Q.append( (0,0) )
    neighbours = [ [-1,0], [0,-1], [1,0], [0,1] ]

    while Q:
        print_2d(dist)
        print("---------")
        i, j = Q.popleft()
        for ngh in neighbours:
            if not 0 <= i+ngh[0] < n or not 0 <= j+ngh[1] < n: continue
            if dist[i+ngh[0]][j+ngh[1]] > dist[i][j]+A[i+ngh[0]][j+ngh[1]]:
                dist[i + ngh[0]][j + ngh[1]] = dist[i][j]+A[i+ngh[0]][j+ngh[1]]
                parent[ i + ngh[0] ][ j + ngh[1] ] = (i,j)
                Q.appendleft( (i + ngh[0], j + ngh[1] ) )

    # print_2d(dist)
    return rec_print(A,parent, n-1, n-1,0)

n = 6
# A = [[randint(1,5) for _ in range(n)] for _ in range(n)]
A = [[1,1,1,1,1],
     [5,5,5,5,1],
     [5,5,5,5,1],
     [5,5,5,5,1],
     [5,5,5,5,1]]
# print_2d(A)
# print("---------")
print(kings_path(A))

