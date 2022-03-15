def print_solution( i, w, h, F, P, W, H ):
    if i==0:
        if w>=W[0] and h>=H[0]: print(0, end=' ')
        return

    if w-W[i]>=0 and h>=H[i]:
        if F[i][w][h] == F[i-1][w-W[i]][h-H[i]] + P[i]:
            print_solution( i-1, w-W[i], h-H[i], F, P, W, H )
            print(i, end=' ')
            return

    print_solution( i-1, w, h, F, P, W, H )


def _rek( i, w, h, F, P, W, H ):

    if i<0: return -1
    if F[i][w][h] != -1:
        return F[i][w][h]

    best = _rek( i-1, w, h, F, P, W, H )
    if w-W[i] >= 0 and h-H[i] >= 0:
        best = max( best, _rek( i-1, w-W[i], h-H[i], F, P, W, H ) + P[i] )

    F[i][w][h] = best
    return F[i][w][h]


def knapsack_2D( P, W, H, maxW, maxH ):
    n = len(P)
    F = [ [ [-1]*(maxH+1) for _ in range(maxW+1) ] for _ in range(n) ]

    for i in range(n): F[i][0][0] = 0

    for h in range(maxH+1):
        for w in range(maxW+1):
            if w >= W[0] and h >= H[0]:
                F[0][w][h] = P[0]
            else: F[0][w][h] = 0

    best = _rek( n-1, maxW, maxH, F, P, W, H )
    print_solution(n - 1, maxW, maxH, F, P, W, H )
    print("")
    return best

P = [5,12,7,1,56,4]
W = [1,11,9,4,10,2]
H = [7,13,1,9,27,1]

print(knapsack_2D(P, W, H, 20, 35))