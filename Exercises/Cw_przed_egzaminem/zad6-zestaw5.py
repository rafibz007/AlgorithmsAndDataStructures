"""

f(i) - minimalna ilosc monet potrzebna aby wydac kwote i

f(i) = min( f(i-c)+1 )    c - moneta w zbiorze S

f(T) - rozwiazanie

"""


def coins(S,T):

    def get_solution(i):
        nonlocal W, solution

        if W[i] is None: return

        solution.append( i-W[i] )
        get_solution(W[i])


    def f(i):
        nonlocal S, F, W, inf

        if i < 0: return inf
        if F[i] < inf:
            return F[i]

        best = inf
        for c in S:
            q = f(i-c)+1
            if best > q:
                best = q
                W[i] = i-c


        F[i] = best
        return best

    inf = float("inf")
    W = [None] * (T + 1)
    F = [inf]*(T+1)
    F[0] = 0

    best = f(T)
    solution = []
    get_solution(T)
    print(W)
    return best, solution

S = [1,5,8]
T = 15
print(coins(S,T))
