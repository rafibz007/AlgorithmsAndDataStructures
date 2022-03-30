def print_solution( i, g, d, F, A, L ):
    if i > 0:
        if g+A[i-1] <= L and F[i-1][g+A[i-1]][d]:
            print_solution( i-1, g+A[i-1], d, F, A, L )
            print(i,": G", sep='')
        elif d+A[i-1] <= L and F[i-1][g][d+A[i-1]]:
            print_solution(i-1, g, d+A[i-1], F, A, L)
            print(i, ": D", sep='')

def _rek( i, g, d, F, A, L ):
    if i < 0: return False
    if F[i][g][d] is not None:
        return F[i][g][d]

    q = False
    if g+A[i-1] <= L: q = q or _rek( i-1, g+A[i-1], d, F, A, L )
    if not q and d+A[i-1] <= L: q = q or _rek( i-1, g, d+A[i-1], F, A, L )

    F[i][g][d] = q
    # print(i, q)
    return F[i][g][d]

def cars( A, L ):

    n = len(A)
    F = [ [ [None]*(L+1) for _ in range(L+1) ] for _ in range(n+1) ]

    # for i in range(L+1):
    #     for j in range(L+1):
    #         F[0][i][j] = True
    F[0][L][L] = True



    for k in range(n, -1, -1):
        for g in range(L+1):
            for d in range(L+1):
                if _rek( k, g, d, F, A, L ):
                    print_solution( k, g, d, F, A, L)
                    return k



A = [ 1, 2, 3, 3, 7 ]
print(cars(A, 5))