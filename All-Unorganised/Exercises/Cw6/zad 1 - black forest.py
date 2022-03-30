def print_solution( i, F ):
    if i < 2:
        if   C[1] > C[0] and C[i] > 0: print(1, end=' ')
        elif C[0] > C[1] and C[0] > 0: print(0, end=' ')
        return


    if F[i] == F[i-2] + C[i]:
        print_solution( i-2, F )
        print(i, end=' ')
    else:
        print_solution( i-1, F )


def cut_trees( C ):
    n = len(C)
    F = [-1]*n

    F[0] = max( 0, C[0] )
    F[1] = max( 0, C[0], C[1] )

    for i in range( 2, n ):
        F[i] = max( F[i-1], F[i-2]+C[i] )

    print( F[n-1] )
    print_solution(n-1, F)


C = [ 2, 4, 5, 100, 15, 4, 12 ]
cut_trees(C)