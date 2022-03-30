def print_2d( T ):
    for t in T:
        print(t)


def print_solution( i, j, A, F ):
    if i > 0:
        for k in range(1, i+1):
            if j+k-A[i] <= 0: continue
            if F[i][j] == F[i-k][j+k-A[i]]+1:
                print_solution( i-k, j+k-A[i], A, F )
                break
    print(i, end=' ')


def _rek( i, j, A, F, inf ):
    # if i < 0: print(i)
    if j <= 0 or j > len(F): return inf
    if F[i][j] != inf: return F[i][j]

    best = inf
    for k in range(1,i+1):
        if k > j+k-A[i]: continue #jezeli dlugosc skoku jest wieksza nic energia na poprzednim polu to nie sprawdzam
        best = min(best, _rek(i-k, j+k-A[i], A, F, inf)+1)
        # if best ==1: print( f"i:{i}  -j:{j}  -i-k:{i-k}  -A[i]:{A[i]}  -j+k-A[i]:{j+k-A[i]}  -best:{best}" )

    F[i][j] = best
    return F[i][j]

def frog( A ):
    n = len(A)

    inf = n+2
    max_energy = sum(A)

    F = [ [inf]*(max_energy+1) for _ in range(n) ]
    F[0][A[0]] = 0
    # for i in range(1, A[0]+1): F[i][A[0]-i] = 1

    best_index = 0
    for k in range(max_energy+1):
        if _rek(n-1, best_index, A, F, inf) > _rek(n-1, k, A, F, inf):
            best_index = k
        # best = min(best, _rek( n-1, k, A, F, inf ))


    print_solution( n-1, best_index, A, F )
    print("")
    # print_2d(F)
    # print(best_index)
    return F[n-1][best_index]



A = [ 2, 1, 1, 1, 4, 2, 3, 1, 1, 1, 1, 1, 1 ]
print(frog(A))