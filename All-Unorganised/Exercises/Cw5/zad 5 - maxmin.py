
def print_2d( A ):
    for i in range(len(A)):
        print(A[i])

def sum_range( A, i, j ):
    s = 0
    for x in range(i, j+1): s += A[x]
    return s


def print_solution( i, t, S, k ):
    if S[i][t] is None:
        print(f"0..{i}, {i+1}..", end='')
    else:
        print_solution( S[i][t], t-1, S, k )
        print(f"{i}", end='')
        if t<k: print(f", {i+1}..", end='')


def _rek( i, t, F, A, inf, S ):
    if F[i][t] is not None:
        return F[i][t]

    best = -inf
    for k in range(1,i):
        q = min( _rek(i-k, t-1, F, A, inf, S), sum_range(A, i-k+1, i) )
        if best < q:
            best = q
            S[i][t] = i-k
        # print(f"-i: {i}  -t: {t}  -k: {k}  -f({i-k},{t-1}): {_rek(i-k, t-1, F, A, inf)}  -sum: {sum_range(A, i-k+1, i)}  -min:{min( _rek(i-k, t-1, F, A, inf), sum_range(A, i-k+1, i) )}  -best: {best}")

    F[i][t] = best
    return F[i][t]

def minmax( A, k ):
    n = len(A)
    F = [ [None]*(k+1) for _ in range(n) ]

    for i in range(n): F[i][0] = 0
    F[0][1]=A[0]
    for i in range(1,n): F[i][1] = F[i-1][1] + A[i]

    inf = sum(A)+1

    S = [ [None]*(k+1) for _ in range(n) ]

    best = _rek(n-1, k, F, A, inf, S)
    print_solution(n-1, k, S, k)
    print("")

    return best


A = [ 5, 2, 7, 1, 6, 3, 8, 4, 2, 7 ]
# print(sum(A))
# print(A)
print(minmax(A, 4))