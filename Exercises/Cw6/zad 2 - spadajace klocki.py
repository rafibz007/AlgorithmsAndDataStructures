def if_a_contains_b( a, b ):
    return a[0] <= b[0] and b[1] <= a[1]


def index_max( F ):
    index = 0
    for i in range( 1, len(F) ):
        if F[index] < F[i]: index = i
    return index


def print_solution( i, R ):
    if R[i] > -1:
        print_solution( R[i], R )
    print( i, end=' ' )


def blocks( S ):
    n = len(S)

    F = [1]*n

    R = [-1]*n

    for i in range(n):
        best = 1
        for j in range(n):
            if i == j: continue
            if if_a_contains_b( S[j], S[i] ):
                q = F[j] + 1
                if best < q:
                    best = q
                    R[i] = j
                # best = max( best, F[j]+1 )
        F[i] = best

    max_index = index_max( F )
    print_solution( max_index, R )
    print("")
    return F[n-1]



S = [ [-1, 3], [0, 5], [1, 11], [2, 4], [2, 9], [5, 8], [6, 7] ]
print(blocks(S))

