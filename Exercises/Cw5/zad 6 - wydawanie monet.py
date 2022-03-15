def get_solution( i, F, S, R ):
    if i > 0:
        for v in S:
            if F[i] == F[i-v]+1:
                get_solution( i-v, F, S, R )
                R.append(v)
                break

def _rek( i, F, S, inf):
    if i < 0: return inf

    if F[i] != inf:
        return F[i]

    # print(S)
    v_min = inf
    for v in S:
        v_min = min( v_min, _rek(i-v, F, S, inf)+1 )

    F[i] = v_min
    return F[i]

def find( S, T ):
    inf = int(T // min(S)) + 2
    n = T+1
    F = [inf]*n

    F[0] = 0

    best = _rek(T, F, S, inf)

    R = []
    get_solution( n-1, F, S, R )
    print(R)
    return best


S = [1, 5, 8]
print(find(S, 15))