"""

f(i,w,h) - maksymalny zysk jaki mozna osiagnac biorac do i-tego przedmiotu, o dostepnej wadze w
           i dostepnej wysokosci h

f(i,w,h) = max(  f(i-1,w,h), f(i-1,w-W[i],h-H[i])+P[i]  )

f(0,w,h) = P[0] | w>=W[0] ^ h>=H[0]
f(0,w,h) = 0 | w<W[0] ^ h<H[0]
"""

def knapsack_3d(P,W,H, maxW, maxH):

    def get_solution(i,w,h):
        nonlocal F,P,W,H,S

        if i > 0:
            if w-W[i] >= 0 and h-H[i] >= 0 and F[i][w][h] == F[i-1][w-W[i]][h-H[i]]+P[i]:
                get_solution(i-1,w-W[i],h-H[i])
                S.append(i)
            else:
                get_solution(i-1, w, h)

        else:
            if W[0] <= w and H[0] <= h:
                S.append(i)



    def f(i,w,h):
        nonlocal F,P,W,H, inf

        if w < 0 or h < 0 or i<0:
            return -inf

        if F[i][w][h] > -inf:
            return F[i][w][h]

        F[i][w][h] = max( f(i-1,w,h), f(i-1,w-W[i],h-H[i])+P[i] )
        return F[i][w][h]


    n = len(P)


    inf = float("inf")

    F = [  [ [-inf]*(maxH+1) for _ in range(maxW+1) ] for _ in range(n)  ]

    for w in range(maxW+1):
        for h in range(maxH+1):
            if w >= W[0] and h >= H[0]:
                F[0][w][h] = P[0]
            else: F[0][w][h] = 0

    S = []
    best = f(n-1, maxW, maxH)
    get_solution(n-1, maxW, maxH)
    return best, S


P = [5,12,7,1,56,4]
W = [1,11,9,4,10,2]
H = [7,13,1,9,27,1]

print(knapsack_3d(P, W, H, 20, 35))

