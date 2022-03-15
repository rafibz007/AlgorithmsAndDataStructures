def print_2d( A ):
    for i in range(len(A)):
        print(A[i])

def find( S, n ):
    F = [ [None]*n for _ in range(n) ]


    #zaleznie od interpretacji czy wchodzimy na pole (1,1) zaczynajac czy na nim stoimy i nie trzeba go dodawac
    F[0][0]=0

    s = 0
    for i in range(1,n):
        s += S[0][i]
        F[0][i] = s

    s = 0
    for i in range(1,n):
        s += S[i][0]
        F[i][0] = s



    for i in range(1,n):
        for j in range(1,n):
            F[i][j] = min( F[i-1][j], F[i][j-1] ) + S[i][j]

    print_2d(F)

    return F[n-1][n-1]


S = [[5, 6, 70],
     [1, 22, 1],
     [8, 9, 2]]

print(find(S, 3))