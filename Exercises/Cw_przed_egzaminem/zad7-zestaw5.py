"""

f(i,j) - najlepsza sciezka z polq (1,1) na pole (i,j)

f(i,j) = min(f(i-1,j), f(i,j-1)) + A[i][j]

"""


def path( A ):

    n = len(A)
    inf = float("inf")
    F = [ [inf]*(n+1) for _ in range(n+1) ]

    F[1][1] = A[0][0]

    for i in range(1,n+1):
        for j in range(1,n+1):
            F[i][j] = min( F[i][j], F[i-1][j]+A[i-1][j-1], F[i][j-1]+A[i-1][j-1] )

    return F[n][n]


A = [ [0,1,1],
      [2,2,100],
      [100,0,0]]

print(path(A))