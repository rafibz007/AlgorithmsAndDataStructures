import knapsack2
from random import randint


def print_2d(tab):
    for i in range(len(tab)): print(tab[i])

def knapsack(P, W, MaxW):

    n = len(W)

    F = [ [0]*(MaxW+1) for _ in range(n) ]
    # print(F)

    for w in range( W[0], MaxW+1 ): F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, MaxW+1):

            F[i][w] = F[i-1][w]

            if w >= W[i]:
                F[i][w] = max( F[i][w], F[i-1][w-W[i]] + P[i] )


    T = get_solution(F,W,P,n-1,MaxW)
    total_price = 0
    for i in range(len(T)): total_price += P[T[i]]

    return total_price, T


def get_solution(F, W, P, i, w):

    if i < 0: return []

    if i == 0:
        if w >= W[0]: return [0]
        return []

    if w >= W[i] and F[i][w] == F[i-1][w-W[i]]+P[i]:
        return get_solution(F,W,P,i-1,w-W[i])+[i]

    return get_solution(F,W,P,i-1,w)

n = 5
k = 100
# P = [10,8,4,5,3,7]
# W = [4,5,12,9,1,13]
for _ in range(k):
    P = [ randint(1, 20) for _ in range( n ) ]
    W = [ randint(1, 20) for _ in range( n ) ]
    MaxW = 24

    s1 = knapsack(P,W,MaxW)
    s2 = knapsack2.knapsack2(P,W,MaxW)
    if s1 != s2: print("s1: ",s1, " | s2: ",s2, " | P: ",P , " | W: ", W)










