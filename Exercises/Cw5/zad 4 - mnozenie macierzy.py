def _rek( i, j, F, P):
    if F[i][j] != -1 or i == j:
        return F[i][j]

    best = _rek(i,i,F,P) + _rek(i+1,j,F,P) + P[i]*P[i+1]*P[j+1]
    for k in range(i+1, j):
        q = _rek(i,k,F,P) + _rek(k+1,j,F,P) + P[i]*P[k+1]*P[j+1]
        if q < best: best = q

    F[i][j] = best
    return F[i][j]

def print_solution( i, j, F, P ):
    if i == j: return
    for k in range( i, j ):
        if F[i][j] == F[i][k] + F[k+1][j] + P[i]*P[k+1]*P[j+1]:
            print_solution(i, k, F, P)
            print_solution(k+1, j, F, P)
            if i+1 == k+1 and k+2 == j+1:
                print(f" A({i+1}) * A({k+2}) ")
            elif i+1 == k+1:
                print(f" A({i + 1}) * A({k + 2}-{j + 1}) ")
            elif k+2 == j+1:
                print(f" A({i + 1}-{k + 1}) * A({j + 1}) ")
            else:
                print(f" A({i+1}-{k+1}) * A({k+2}-{j+1}) ")
            break



def matrix_mult_min_cost( P ):
    n = len(P)-1
    F = [ [-1]*n for _ in range(n) ]

    for i in range(n): F[i][i] = 0

    best = _rek(0, n - 1, F, P)
    print_solution(0, n-1, F, P)

    return best



P = [ 20, 40, 30, 15, 2, 13, 7, 15, 50, 70 ]
print(matrix_mult_min_cost(P))