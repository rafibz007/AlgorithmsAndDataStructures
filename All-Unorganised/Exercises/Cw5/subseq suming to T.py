def print_2d(T):
    tab = [ T[i] for i in range(len(T)) ]
    for subtab in tab:
        for j in range(len(subtab)):
            if subtab[j] is True: subtab[j] = 1
            else: subtab[j] = 0

    for i in range(len(tab)): print(tab[i])

def check(A, T):
    n = len(A)
    F = [ [False]*(T+1) for _ in range( n )]

    if T == 0 and 0 in A: return True
    elif T == 0: return False

    for i in range( n ):   F[i][0] = (A[i] == 0)
    for v in range( T+1 ): F[0][v] = (A[0] == v)

    for i in range( 1, n ):
        for v in range( 1, T+1 ):

            F[i][v] = ( F[i-1][v] or A[i] == v )

            if v-A[i] >= 0:
                F[i][v] = ( F[i][v] or F[i-1][v-A[i]] )

            if v == T and F[i][v]: return True

    return F[n-1][T]





A = [ 4, 234 ,5 ,6346 ,45 ,745 ,7 ,45 ,7, 0, 2]
T = sum(A)
print(check(A, T), T)


