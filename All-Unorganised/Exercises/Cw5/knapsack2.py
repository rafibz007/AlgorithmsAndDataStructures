def print_2d(tab):
    for i in range(len(tab)): print(tab[i])


def knapsack2(P, W, MaxW):

    n = len(W)
    price_sum = sum(P)
    inf = sum(W)+1

    F = [ [0]*(price_sum+1) for _ in range(n) ]
    # print(F)

    # for p in range( 1, P[0]+1 ): F[0][p] = W[0]
    # for p in range( P[0]+1, price_sum+1 ): F[0][p] = inf
    for p in range( 1, price_sum+1 ): F[0][p] = inf
    F[0][P[0]] = W[0]

    for i in range(1, n):
        for p in range(1, price_sum+1):

            F[i][p] = F[i-1][p]

            if p >= P[i]:
                F[i][p] = min(F[i][p], F[i-1][p-P[i]] + W[i])


    for p in range(price_sum, -1, -1):
        for i in range(n):
            if F[i][p] <= MaxW:

                S = get_solution2(F, W, P, i, p)
                # print_2d(F)
                return p, S

    return 0


def get_solution2(F, W, P, i, p):

    if i < 0: return []

    if i == 0:
        if p == P[0]: return [0]
        return []

    if p >= P[i] and F[i][p] == F[i-1][p-P[i]] + W[i]:
        return get_solution2(F, W, P, i-1, p-P[i]) + [i]

    return get_solution2(F, W, P, i-1, p)

if __name__ == "__main__":
    P = [10,8,4,5,3,7]
    W = [4,5,12,9,1,13]

    print(knapsack2(P,W,24))










